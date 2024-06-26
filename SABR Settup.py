import streamlit as st
import pandas as pd
import time
from chatgpt_coder import ChatGPTCoder

# Initialize the ChatGPTCoder with your OpenAI API key
gpt_coder = ChatGPTCoder(st.secrets["OPENAI_API_KEY"])


st.title("Auto SABR Coding")
st.markdown("Prototype app for testing automatic SABR coding using LLMs.")
with st.expander("Prompting Scheme"):
    st.header("Prompt template")
    st.caption(
        "The system prompt dynamically changes depedning on the code and then each then each utterance is checked against the prompt."
    )
    st.caption(
        "The delimiters are used for pasring i.e., seperating the code (1 or X) from the rest of the output. OpenAI have just added a new JSON mode which could make this easier."
    )
    st.code(
        """
        - Task: You are a qualitative research assistant coding utternaces for meaning related codes
        Analyze the utterance against coding criteria. 
        The aim of this coding is to help researchers measure and examines qualities of teacher and child talk. 
        Use the given rules for applying codes from the coding manual, deliminate by four hashtags i.e. {delimiter}, to assess wether the utternace meets the criteria. 
            
            {delimiter}
            Coding Manual: 
            - Meaning-related code Name: {code_name}. 
            - Definition: {code_definition}.
            - Keywords: {keywords}. 
            - Code Notes: {code_notes}. 
            - Example: {example}. 
            {delimiter}

            Follow these steps. \
            
            Step 1: {delimiter} Analyze the presence of keywords and review code notes to conclude whether the utterance meets the criteria for the code. \

            Step 2: {delimiter} determine if code applies to utterance 
            * Respond with '1' followed by a brief explanation if the utterance meets the criteria. 
            * Respond with 'X' followed by a brief explanation if it does not. 
            * Only respond with an '1' or 'X' and nothing else 

            Use the following format: 
            Step 1:{delimiter} <Your decision-making process analysis. Summarize how the coding manual lead you to conclude whether the utterance meets the criteria for the code.> \

            Step 2:{delimiter}<Your final code decision. Only include '1' if the utterance meets the criteria, or 'X' if it does not. No additional text should be here.> \

            Example input: 
            Can you think of the names of other plants that need to grow on many acres of land?

            Example Output: 
            Step 1:{delimiter} This utterance meets the criteria for the Compare/Contrast code as it explicitly refers to sharing food by giving everyone a fraction of it instead of the whole thing, highlighting a comparison between sharing practices for certain food items. \

            Step 2:{delimiter} 1

            Make sure to include {delimiter} to separate every step.
            """
    )
    st.header("Code w/variables example")
    st.caption("Taxonomy taken from SABR Transcript Coding Manual")
    st.code(
        '''
        code_name = "Sequence/Temporal"
        
        code_definition = "Involves explicit discussions of when events occurred in a sequence or references to time."
        
        keywords = 
        """
        Keywords sequential order: first, second, third, next, last, begin (beginning), middle, end, ,  last, after, earlier, before, final (finally) 
        Keywords time: day (yesterday, today, Monday and all variations), tomorrow, time (meantime, sometime), minute, second (as in 60 seconds), morning, daytime, evening, nighttime
        """
        
        code_notes = 
        """
        * Reference to time and temporal ordering 
        * These are tools of good writers/storytellers and are abstract to young children 
        * Reference to a sequence/temporal ordering of events within or across pages 
        * Reference to the timing or duration of events 
        * References to time can include specifically telling time or using a calendar, or more general orientations in time
        * Do not code temporal language that is behavior-related or speed in relation to time. 
        """
        
        example = ""
        '''
    )


with st.expander("Chain-of-thought Prompting"):
    st.markdown(
        "Prompting scheme modeled after a paper on chain of thought prompting -- a series of intermediate reasoning steps -- significantly improves the ability of large language models to perform complex reasoning"
    )

    st.markdown("Can definetly be imporved with testing.")
    st.caption(
        "Reference  \nWei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., ... & Zhou, D. (2022). Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems, 35, 24824-24837. https://doi.org/10.48550/arXiv.2201.11903 "
    )

# File uploader widget
uploaded_file = st.file_uploader("Choose an Excel file")
if uploaded_file is not None:
    # Check file extension
    if not uploaded_file.name.endswith(".xlsx") and not uploaded_file.name.endswith(
        ".xls"
    ):
        st.error("Unsupported file format! Please upload an Excel file.")
    else:
        df = pd.read_excel(uploaded_file)

    # Convert every column into a string for consistent processing
    for column in df.columns:
        df[column] = df[column].astype(str)

    # Display the DataFrame for the user to review
    st.dataframe(df)

    # Options for user to select codes to apply
    code_options = [
        "Sequence/Temporal",
        "Compare/Contrast",
        "Cognition",
        "Desires/Preferences",
        "Feelings/Emotions",
        "Judgments/Perspectives",
        "Causal Effects & Problem Solving",
        "Predictions/Forecast",
        # "Define Vocabulary",
        "Making Connections",
        "Building Knowledge",
    ]

    selected_codes = st.multiselect(
        "Select the codes to apply:", code_options, default=code_options
    )

    # Toggle for explanations
    include_explanations = st.checkbox("Include explanations with codes")

    # Button to start coding process
    if st.button("Apply Coding"):
        start_time = time.time()
        with st.spinner("Coding in progress... Please wait."):
            for i, row in df.iterrows():
                utterance = row["Utterance/Idea Units"]

                if "Sequence/Temporal" in selected_codes:
                    code_response, explanation = gpt_coder.code_sequence_temporal(
                        utterance
                    )
                    df.at[i, "Sequence_Temporal"] = code_response
                    if include_explanations:
                        df.at[i, "Sequence_Temporal Explanation"] = explanation

                if "Compare/Contrast" in selected_codes:
                    code_response, explanation = gpt_coder.code_compare_contrast(
                        utterance
                    )
                    df.at[i, "Compare_Contrast"] = code_response
                    if include_explanations:
                        df.at[i, "Compare_Contrast Explanation"] = explanation

                if "Cognition" in selected_codes:
                    code_response, explanation = gpt_coder.code_cognition(utterance)
                    df.at[i, "Cognition"] = code_response
                    if include_explanations:
                        df.at[i, "Cognition Explanation"] = explanation

                if "Desires/Preferences" in selected_codes:
                    code_response, explanation = gpt_coder.code_desire_preferences(
                        utterance
                    )
                    df.at[i, "Desires_Preferences"] = code_response
                    if include_explanations:
                        df.at[i, "Desires_Preferences Explanation"] = explanation

                if "Feelings/Emotions" in selected_codes:
                    code_response, explanation = gpt_coder.code_feeling_emotions(
                        utterance
                    )
                    df.at[i, "Feelings_Emotions"] = code_response
                    if include_explanations:
                        df.at[i, "Feelings_Emotions Explanation"] = explanation

                if "Judgments/Perspectives" in selected_codes:
                    code_response, explanation = gpt_coder.code_judgments_perspectives(
                        utterance
                    )
                    df.at[i, "Judgments_Perspectives"] = code_response
                    if include_explanations:
                        df.at[i, "Judgments_Perspectives Explanation"] = explanation

                if "Causal Effects & Problem Solving" in selected_codes:
                    code_response, explanation = (
                        gpt_coder.code_causal_effects_problem_solving(utterance)
                    )
                    df.at[i, "CausalEffects_ProblemSolve"] = code_response
                    if include_explanations:
                        df.at[i, "CausalEffects_ProblemSolve Explanation"] = explanation

                if "Predictions/Forecast" in selected_codes:
                    code_response, explanation = gpt_coder.code_predictions_forecast(
                        utterance
                    )
                    df.at[i, "Predictions_Forecast"] = code_response
                    if include_explanations:
                        df.at[i, "Predictions_Forecast Explanation"] = explanation

                # if "Define Vocabulary" in selected_codes:
                #     code_response, explanation = gpt_coder.code_define_vocabulary(
                #         utterance
                #     )
                #     df.at[i, "DefineVocabulary"] = code_response
                #     if include_explanations:
                #         df.at[i, "DefineVocabulary Explanation"] = explanation

                if "Making Connections" in selected_codes:
                    code_response, explanation = gpt_coder.code_making_connections(
                        utterance
                    )
                    df.at[i, "MakingConnections"] = code_response
                    if include_explanations:
                        df.at[i, "MakingConnections Explanation"] = explanation

                if "Building Knowledge" in selected_codes:
                    code_response, explanation = gpt_coder.code_building_knowledge(
                        utterance
                    )
                    df.at[i, "BackgroundKnowledge"] = code_response
                    if include_explanations:
                        df.at[i, "BackgroundKnowledge Explanation"] = explanation

            end_time = time.time()  # Step 3
            duration_seconds = end_time - start_time  # Step 4
            duration_minutes = duration_seconds / 60  # Convert seconds to minutes
            st.success(
                f"Coding completed successfully in {duration_minutes:.2f} minutes!"
            )

            # Display the updated DataFrame
            st.dataframe(df)

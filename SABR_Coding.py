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
    st.code(
        '''
        system_prompt = 
        f"""
        - Task: Analyze the utterance against coding criteria.
        - Code Name: {code_name}.
        - Keywords: {keywords}.
        - Definition: {code_definition}.
            * Note: Keywords should be used as indicators of the underlying concept or theme being discussed. The presence of a single keyword may be sufficient, but consider the overall context of the utterance. Ambiguous cases should be carefully evaluated.
        - Notes: {code_notes}.
        - Example: {example}.
        - Instruction: 
            * Respond with '1' followed by a detailed explanation if the utterance meets the criteria.
            * Respond with 'X' followed by a detailed explanation if it does not.
            * Always start your response with '1' or 'X'.
        """
        '''
    )
    st.header("Code w/variables example")
    st.caption("Taxonomy taken from SABR Transcript Coding Manual")
    st.code(
        '''
        code_name = "Sequence/Temporal"
        code_definition = "Involves explicit discussions of when events occurred in a sequence or references to time."
        keywords = """
        Keywords sequential order: first, second, third, next, last, begin (beginning), middle, end, ,  last, after, earlier, before, final (finally) 
        Keywords time: day (yesterday, today, Monday and all variations), tomorrow, time (meantime, sometime), minute, second (as in 60 seconds), morning, daytime, evening, nighttime
        """
            code_notes = """
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

                if "Define Vocabulary" in selected_codes:
                    code_response, explanation = gpt_coder.code_define_vocabulary(
                        utterance
                    )
                    df.at[i, "DefineVocabulary"] = code_response
                    if include_explanations:
                        df.at[i, "DefineVocabulary Explanation"] = explanation

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
            st.success(f"Coding completed successfully in {duration_minutes:.2f} minutes!")

            # Display the updated DataFrame
            st.dataframe(df)

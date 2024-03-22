import streamlit as st
import pandas as pd
from chatgpt_coder import ChatGPTCoder

# Initialize the ChatGPTCoder with your OpenAI API key
gpt_coder = ChatGPTCoder(st.secrets["OPENAI_API_KEY"])

# File uploader widget
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Load the uploaded file into a DataFrame
    df = pd.read_excel(uploaded_file)

    # Convert every column into a string for consistent processing
    for column in df.columns:
        df[column] = df[column].astype(str)

    # Display the DataFrame for the user to review
    st.dataframe(df)

    # Options for user to select codes to apply
    code_options = ["Cognition", "Desires/Preferences"]
    selected_codes = st.multiselect("Select the codes to apply:", code_options)

    # Toggle for explanations
    include_explanations = st.checkbox("Include explanations with codes")

    # Initialize new columns based on selected options
    for code in selected_codes:
        df[f"{code} Code"] = "Pending"
        if include_explanations:
            df[f"{code} Explanation"] = ""

    # Button to start coding process
    if st.button("Apply Coding"):
        for i, row in df.iterrows():
            utterance = row["Utterance/Idea Units"]

            if "Cognition" in selected_codes:
                code_response, explanation = gpt_coder.code_cognitive(utterance)
                df.at[i, "Cognition Code"] = code_response
                if include_explanations:
                    df.at[i, "Cogniton Explanation"] = explanation

            # Example for another coding function, similar to 'code_cognitive'
            # if "Desires/Preferences" in selected_codes:
            # Apply your method for desires/preferences coding here
            # Update the DataFrame similarly

        # Display the updated DataFrame
        st.dataframe(df)

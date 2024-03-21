import streamlit as st
import pandas as pd
import openai


class ChatGPTProcessor:
    def __init__(self, openai_api_key):
        self.client = openai.OpenAI(api_key=openai_api_key)
        openai.api_key = openai_api_key

    def generate_code(
        self,
        utterance,
        code_name,
        code_definition,
    ):
        """
Generate code x or 1, input your utterance and then the code definition
        """

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a qualitiave resaerch assistant coding utterances for {code_name}. Code definition/instructions: {code_definition}. The user input will be just the utterance. Respond with a 1 if the response meets the definition criteria, respond with an x if it does not."},
                    {"role": "user", "content": utterance},
                    max_tokens=60,
                ],
            )
            return response.choices[0].message.content
        
        except Exception as e:
            print(f"Error in generating code: {e}")
            return 'Error'  # Consider handling errors appropriately.


class FormAutoCoder(ChatGPTProcessor):
    def __init__(self, openai_api_key):
        super().__init__(openai_api_key=openai_api_key)
        

    def code_comment(self, utterance):
        # Example criterion: does the utterance contain a comment keyword?
        code_name = "comment"
        code_definition = """
        * These are the most common utterance
        form.
        * Declarative sentences that convey
        information or make statements.
        * They do not demand a response from
        the listener.
        * Comments end in a period or exclamation
        mark.
        * If an utterance does not neatly fit one of these
        utterance forms, assume it is a comment by
        default.
        """
        code = self.generate_code(utterance, code_name, code_definition)

# Keyword coding
def code_wh_question(utterance):
    keywords = ['who', 'what', 'when', 'where', 'which']
    return 1 if any(keyword.lower() in utterance.lower() for keyword in keywords) else 'x'

def code_why_question(utterance):
    keywords = ['why']
    return 1 if any(keyword.lower() in utterance.lower() for keyword in keywords) else 'x'


form_auto_coder = FormAutoCoder(openai_api_key=st.secrets(["OPENAI_API_KEY"]))

st.title("Automated SABR Coding")
st.markdown("ChatGPT for qualitative coding rototype ")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    # Example of processing each row (simplified and needs to be adapted)

    st.dataframe(df)  # Corrected method to display DataFrame

    # for index, row in df.iterrows():
    #     df.at[index, 'Comment Code'] = auto_coder.code_comment(row['Utterance'])

import openai


class ChatGPTCoder:
    def __init__(self, openai_api_key):
        self.client = openai.OpenAI(api_key=openai_api_key)
        openai.api_key = openai_api_key

    def generate_code_no_explination(
        self, utterance, code_name, keywords, code_definition, code_notes, example
    ):
        """
        Generate code '1' if the utterance meets the code definition criteria, or
        'X' if it does not, based on keywords, code definition, and code notes.
        """

        code_notes += "\nKeywords should be used as indicators of the underlying concept or theme being discussed. The presence of a single keyword may be sufficient, but consider the overall context of the utterance. Ambiguous cases should be carefully evaluated."

        try:
            system_prompt = (
                f"Analyze if the utterance fits the coding criteria for '{code_name}' based on the keywords and definitions provided. "
                f"For instance, {example}"
                f"Do not provide any reasoning or explanation in your response. "
                f"If the utterance meets the criteria based on the keywords '{keywords}', code definition '{code_definition}', and notes '{code_notes}', an XXX in the utterance indicates an inaudible word."
                f"simply respond with a '1'. If it does not meet the criteria, respond with an 'X'."
            )

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": utterance},
                ],
                max_tokens=10,  # Reduced max_tokens as the expected output is very short
            )

            # Extract and return only '1' or 'X' from the response
            code_response = response.choices[0].message.content.strip().upper()
            # Ensure the response is strictly '1' or 'X'
            return "1" if code_response == "1" else "X"

        except Exception as e:
            print(f"Error in generating code: {e}")
            return "Error"  # Adjust according to how you want to handle errors.

    def generate_code(
        self, utterance, code_name, keywords, code_definition, code_notes, example
    ):
        """
        Generate code '1' or 'X' if the utterance meets or does not meet the code definition criteria, respectively, based on keywords, code definition, and code notes. Always provide an explanation for the decision.
        """

        # Extend code_notes with a directive to always include an explanation after the code
        code_notes += "\nKeywords should be used as indicators of the underlying concept or theme being discussed. The presence of a single keyword may be sufficient, but consider the overall context of the utterance. Ambiguous cases should be carefully evaluated."

        try:
            system_prompt = (
                f"Analyze if the utterance fits the coding criteria for '{code_name}' based on the keywords and definitions provided. For instance, {example} "
                f"Respond with a '1' followed by a detailed explanation if the utterance meets the criteria based on the keywords '{keywords}', code definition '{code_definition}', and notes '{code_notes}'. If it does not meet the criteria, respond with an 'X' followed by a detailed explanation."
                f"Always begin respond with a '1' or 'X'. '1' if it meets the criteria; 'X' if it does not meet the criteria."
            )

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": utterance},
                ],
                max_tokens=100,  # Increased max_tokens to accommodate the explanation
            )

            # Extract the response, which includes both the code and the explanation
            full_response = response.choices[0].message.content.strip()

            # Split the response to separate the code ('1' or 'X') from the explanation
            code, explanation = full_response[0], full_response[1:].strip()

            # Ensure the code is strictly '1' or 'X'
            code = "1" if code == "1" else "X"

            return code, explanation

        except Exception as e:
            print(f"Error in generating code with explanation: {e}")
            return (
                "Error",
                "An error occurred while generating the code and explanation.",
            )  # Adjust according to how you want to handle errors.

    def code_cognitive(self, utterance):
        code_name = "Cognition"
        keywords = """
    Keywords: learn, think, know, believe, make believe, plan, pretend, doubt, marvel, remember, recall, forget, guess, dream, visualize, imagine, understand, figure it out, have in mind, change mind, realize, consider, come up with, decide, decision, pick (meaning choice), choice, choose
    False belief keywords: really, real, reality, in fact, actual, actually, truth, truly, false, wrong, incorrect
    Possible keywords: try, figure out, find out, surprise, wonder
    """
        code_definition = "Indicates explicit reference to cognitive processes."
        code_notes = """
    * Naming or describing character/self/others’ cognition
    * Frequent inferences about characters’ cognition pertain to their mental processes as signaled by keywords 
    * Using keywords to describe teachers/students own thinking is also coded here 
    * Two keywords (surprise and wonder) can represent cognitive processes or emotions. An active process of wondering shown in the verb form is Cognition. 
    * This code is given even if the cognitive term was explicitly stated in the text because of the presence of mental state language
    * This excludes formulaic responses like “I don’t know” and “I (don’t) think so.”
    """
        example = "'I know what it is, I know what it is, but I forgot the XXX.' gets a '1' because cognition because the speaker is referring to their cognitive process."

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )

        return code_response, explanation  # Returning both code and explanation

    def code_desire_preferences(self, utterance):
        code_name = "Desires_Preferences"
        keywords = """
placeholder
"""
        code_definition = "Involves wishing or wanting something, or expressing a greater liking for one alternative over another."
        code_notes = """
placeholder
"""
        code_response = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes
        )

        return code_response

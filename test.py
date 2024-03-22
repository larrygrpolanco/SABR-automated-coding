
# Chain of Thought example, good for testing and validation
def generate_code(self, utterance, code_name, keywords, code_definition, code_notes):
    """
    Generate code x or 1, based on whether the utterance meets the code definition
    for a given code name, considering specified keywords and code notes.
    """

    try:
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"Let's analyze step by step. You're coding utterances for {code_name}. Consider the keywords: {keywords}. Then, apply the code definition: {code_definition}. Also, keep in mind the notes: {code_notes}. For the given utterance, decide if it meets the definition criteria (respond with a 1) or if it does not (respond with an x). Please explain your reasoning briefly.",
                },
                {"role": "user", "content": utterance},
            ],
            max_tokens=250,
        )
        # The response includes the decision ('1' or 'x') and a brief explanation.
        return response.choices[0].message.content

    except Exception as e:
        print(f"Error in generating code: {e}")
        return "Error"  # Consider handling errors more appropriately.

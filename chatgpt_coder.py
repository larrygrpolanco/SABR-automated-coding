import openai


class ChatGPTCoder:
    def __init__(self, openai_api_key):
        self.client = openai.OpenAI(api_key=openai_api_key)
        openai.api_key = openai_api_key

    def generate_code(
        self, utterance, code_name, keywords, code_definition, code_notes, example
    ):
        """
        Chain of Thought Reasoning
        Generate code '1' or 'X' if the utterance meets or does not meet the code definition criteria, respectively, based on keywords, code definition, and code notes. Always provide an explanation for the decision.
        """

        try:
            delimiter = "####"
            system_prompt = f"""
            - Task: You are a qualitative research assistant coding utternaces for meaning related codes. Analyze the utterance against coding criteria. The aim of this coding is to help researchers measure and examines qualities of teacher and child talk. Use the given rules for applying codes from the coding manual, deliminate by four hashtags i.e. {delimiter}, to assess wether the utternace meets the criteria. \
            
            {delimiter}
            Coding Manual: \
            - Meaning-related code Name: {code_name}. \
            - Definition: {code_definition}. ]
            - Keywords: {keywords}. \
            - Code Notes: {code_notes}. \
            - Example: {example}. \
            {delimiter}

            Follow these steps. \
            
            Step 1: {delimiter} Step 1: Analyze the presence of keywords and review code notes to conclude whether the utterance meets the criteria for the code. \

            Step 2: {delimiter} determine if code applies to utterance \
            * Respond with '1' followed by a brief explanation if the utterance meets the criteria. \
            * Respond with 'X' followed by a brief explanation if it does not. \
            * Only respond with an '1' or 'X' and nothing else \

            Use the following format: \
            Step 1:{delimiter} <Your decision-making process analysis. Summarize how the coding manual lead you to conclude whether the utterance meets the criteria for the code.> \

            Step 2:{delimiter}<Your final code decision. Only include '1' if the utterance meets the criteria, or 'X' if it does not. No additional text should be here.> \

            Example input: \
            Can you think of the names of other plants that need to grow on many acres of land?

            Example Output: \
            Step 1:#### TThis utterance meets the criteria for the Compare/Contrast code as it explicitly refers to sharing food by giving everyone a fraction of it instead of the whole thing, highlighting a comparison between sharing practices for certain food items. \

            Step 2:#### 1

            Make sure to include {delimiter} to separate every step.
            """

            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": utterance},
                ],
                max_tokens=200,  # Increased max_tokens to accommodate the explanation
            )

            # Extract the response, which includes both the code and the explanation
            full_response = response.choices[0].message.content.strip()

            # Split the response to isolate the part after the last delimiter
            code_with_delimiter = full_response.split(delimiter)[-1].strip()

            # Assuming the code ('1' or 'X') is immediately after the last delimiter without additional text
            code = code_with_delimiter[0]  # This should be '1' or 'X'
            explanation = full_response.split(delimiter)[
                :-1
            ]  # This isolates the explanation parts
            explanation = delimiter.join(
                explanation
            ).strip()  # Rejoin the explanation parts without the last segment

            # Ensure the code is strictly '1' or 'X'
            code = "1" if code == "1" else "X"

            return code, explanation

        except Exception as e:
            print(f"Error in generating code with explanation: {e}")
            return (
                "Error",
                "An error occurred while generating the code and explanation.",
            )  # Adjust according to how you want to handle errors.

    def generate_code_basic(
        self, utterance, code_name, keywords, code_definition, code_notes, example
    ):
        """
        Generate code '1' or 'X' if the utterance meets or does not meet the code definition criteria, respectively, based on keywords, code definition, and code notes. Always provide an explanation for the decision.
        """

        try:
            system_prompt = f"""
        - Task: You are a qualitative research assistant coding utternaces from a transcripts. Analyze the utterance against coding criteria. The coding manual is designed to help researchers measure and capture rich language features. Use the code description, deliminated by three forwardlashes, from the coding manual to assess wether the utternace meets the criteria.
        ///
        - Code Name: {code_name}.
        - Keywords: {keywords}.
        - Definition: {code_definition}.
            * Note: Keywords should be used as indicators of the underlying concept or theme being discussed. The presence of a single keyword may be sufficient, but consider the overall context of the utterance. Ambiguous cases should be carefully evaluated.
        - Notes: {code_notes}.
        - Example: {example}.
        ///
        - Instruction: 
            * Respond with '1' followed by a brief explanation if the utterance meets the criteria.
            * Respond with 'X' followed by a brief explanation if it does not.
            * Always start your response with '1' or 'X'.
            """

            response = self.client.chat.completions.create(
                model="gpt-4-turbo-preview",
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

    def code_sequence_temporal(self, utterance):
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

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_compare_contrast(self, utterance):
        code_name = "Compare/Contrast"
        code_definition = "Explicit references to comparison or identification of patterns at any literal or inferential levels."
        keywords = """
    Keywords: like, likewise, similar, same, different, difference, opposites, contrast, compare/comparison, alike, not alike
    Possible keyword: but (when used as conjunction to introduce an explicit comparison with something previously stated)
    """
        code_notes = """
    * Reference to similarities and differences 
    * Matching similar objects, including matching pictured objects in illustration 
    * May include similes and metaphors if they use comparative terms 
    * May identify comparison of mental states or inferential topics 
    * Categorization may seek to build background knowledge 
    * This does not include classifying objects into groups/categories unless comparative terms are used.
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_cognition(self, utterance):
        code_name = "Cognition"
        code_definition = "Indicates explicit reference to cognitive processes."
        keywords = """
    Keywords: learn, think, know, believe, make believe, plan, pretend, doubt, marvel, remember, recall, forget, guess, dream, visualize, imagine, understand, figure it out, have in mind, change mind, realize, consider, come up with, decide, decision, pick (meaning choice), choice, choose
    False belief keywords: really, real, reality, in fact, actual, actually, truth, truly, false, wrong, incorrect
    Possible keywords: try, figure out, find out, surprise, wonder
    """
        code_notes = """
    * Naming or describing character/self/others’ cognition
    * Frequent inferences about characters’ cognition pertain to their mental processes as signaled by keywords 
    * Using keywords to describe teachers/students own thinking is also coded here 
    * Two keywords (surprise and wonder) can represent cognitive processes or emotions. An active process of wondering shown in the verb form is Cognition. 
    * This code is given even if the cognitive term was explicitly stated in the text because of the presence of mental state language
    * This excludes formulaic responses like “I don’t know” and “I (don’t) think so.”
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_desire_preferences(self, utterance):
        code_name = "Desires/Preferences"
        code_definition = "Involves wishing or wanting something, or expressing a greater liking for one alternative over another."
        keywords = """
    Keywords: dislike, don’t like, love, fond, keen, enjoy, want, prefer, favorite, hate, can’t stand, hope, wish
    Possible keyword: like (when meaning preference), need (when communicating a desire)
    """
        code_notes = """
    * Inferring characters’, self, and others’ desires and preferences
    * Includes identifying the character’s intent (action performed intentionally versus involuntarily)
    * Code regardless of whether the desire term was inferred or explicitly stated in the text 
    * Some words indicate modulations of assertions to signal differing preferences (e.g., maybe), but are not standalone keywords 
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_feeling_emotions(self, utterance):
        code_name = "Feelings/Emotions"
        code_definition = (
            "Captures feeling/emotions such as sad, happy, angry or other variations."
        )
        keywords = """
    Keywords: Feel(s)/feeling(s), emotion(s), happy, joyful, serene, calm, relaxed, ecstatic, glad, gleeful, proud, confident; sad, grumpy, pensive, serious, sad, solemn, grieving, depressed, lonely, discouraged, disappointed; fear, worried, apprehensive, scared, afraid, frightened, terrified, anxious, concerned, shy, self-conscious, embarrassed; angry, annoyed, stressed, overwhelmed, frustrated, upset, irritated, mad, furious, crabby, contempt, hatred, aggressive, jealous; anticipation, disappointed, interested, vigilant, optimistic; surprised, excited, startled, dazed, confused, awe; disgusted, bored, apathetic, loathing, remorseful, sorry; trusting, admiration, accepted, secure, loved, thankful, forgiven, miss. 
    Vague emotion keywords: moody, in a good/bad mood, bad tempered, being difficult, not feeling yourself, “getting tired of,” had enough, fed up
    """
        code_notes = """
    * Naming or describing emotional or affective states of self/others/characters
    * This code is marked regardless of whether the emotional state was inferred or whether it was explicitly stated in the text because of the presence of mental state language.
    * Code all basic emotions, more/less intense emotions, combination emotions (contempt), and vague emotional references (good mood).
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_judgments_perspectives(self, utterance):
        code_name = "Judgments/Perspectives"
        code_definition = "Includes opinions, attitudes, and assertions that express character/self/other’s judgments about the quality of something, traits/identity of someone or other attitudes about stimulus/state"
        keywords = """
    Identity keywords: Mean/nice, boss/bossy/bossing, compliant, fair/unfair, fun/boring, beautiful/ugly, brave/timid, “scaredy cat,” egotistic, impulsive, obedient, risky, bossy, agreeable, cool (i.e., trendy), amazing, awesome, friendly, fancy, intelligent, smart, stupid, creative, faithful, dis/honest, loving, nurturing, important, inferior, respectful, powerful, successful; bully
    Quality keywords: Acceptable, inadequate, good/bad/okay, best/worst, perfect/wonderful, horrible, terrible, disaster, should, “supposed to,” must
    Persuasion keywords: Agree/disagree, doesn’t make sense, argue, reject, accept, contend, claim, submit
    Possible keywords: Try, effort, attempt when reference sufficient/good attempts; kind (i.e., caring), “looks like” when making a comparison, “sounds like”
    """
        code_notes = """
    * Reflects differences in human perception because people hold different attitudes, opinions, and tolerances
    * Discussion or statement that passes judgment on someone/something includes rather common judgments such as morality and more complex judgments like beauty, intelligence, etc.
    * References to character/self/other's different perspectives, or comparing perspectives between teachers and students or between two students 
    * Differing social judgments may lead to persuasion and attempts to change opinions
    * Some words indicate modulations of assertions to signal differing perspectives (might, maybe, perhaps, possibly, probably, could be, must, certainly, sure, guess, suppose), but are not standalone keywords; coders must decide within the context whether a judgment was present 
    * Excludes literal/perceptual talk about things that you can see, hear, smell, taste, touch (e.g., big, small). 
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_causal_effects_problem_solving(self, utterance):
        code_name = "Causal Effects & Problem Solving"
        code_definition = "These are inferences on a causal chain between the current, explicit action/event/state and previous text information. Causal effects reference antecedents or consequences/effects of text events or physical states/objects."
        keywords = """
    Causal keywords: because, ‘cause/cuz, why, since, cause, effect, reason, if-then, if/then (on their own if used in a causal manner) 
    Possible keywords: make happen, how, when-then, so (i.e., therefore)
    Problem solving keywords: solve, solution, problem, challenge, trouble, dilemma, conundrum, work out (i.e., solve), resolve, attempt, fix, mend, repair
    Possible keywords: try
    """
        code_notes = """
    Causal Effect Notes:
    * These inferences can identify can explain relations between states or events that occur close together or more distant events in the text. 
    * References to mental causality identify or explain antecedents and consequences of mental states
    * This includes asking for/explaining the how/why of things including cause/effect. Causes are the reason or antecedent/justification for an event. Effects are direct or indirect outcomes/consequences. 
    * Asks for or explains conditions under which certain outcomes do occur (If – then; when – then)
    * Going beyond an initial inference to explain the justification/reasoning behind an inference (why an emotion was inferred; why my judgment is correct)
    Problem Solving Notes:
    * Discussion to identify a problem or solution  
    * Describe obstacles or problems faced by character/self/others 
    * Discussing ways characters might solve problems or reach goals 
    * Some words indicate modulations of assertions to signal different ways to solve problems (might, maybe, perhaps, possibly, probably, could be, must, certainly, sure, guess, suppose), but are not standalone keywords; coders must decide within the context problem solving or causal effects are the topic
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_predictions_forecast(self, utterance):
        code_name = "Predictions/Forecast"
        code_definition = "Inferences on a forecasted causal chain into the future, such as predicting new plans for the character or asking what event will happen next."
        keywords = """
    Keywords/phrases: expect, anticipate, will happen next, could happen next
    Possible phrases: I think ___ will ___, might see __, might have ___
    """
        code_notes = """
    * Predictions identify or explain expected causal chains in future events or plans of characters.
    * Some predictive utterances go beyond making a prediction to explain the rationale for a predictive inference 
    * For teacher comments/declarative statements to be coded as prediction, they must include explicit statement of what they will be looking for 
    * If a teacher revisits a prediction by confirming or revising an earlier hypothesis, mark this code; however, vague confirmations/praise are not coded here 
    * Predicting often occurs before reading (or during a picture walk/text preview) if the teacher models or encourages predicting subsequent story events
    * If a teacher poses a prediction question, code all subsequent answers to that question as prediction. 
    * The phrase “going to/gonna” is not sufficient to use this code. To code this phrase, it requires “going to” + specific prediction or “let’s see” + specific reference 
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_define_vocabulary(self, utterance):
        code_name = "Define Vocabulary"
        code_definition = "Includes asking for or providing a word’s definition or elaborates on word meaning. The focal vocabulary word does not have to be repeated in every utterance to receive this code."
        keywords = """
    Key phrases: What does that word mean? The word ___ means…, “amazing words,” “wondrous words,” “word wizards,” academic vocabulary
    """
        code_notes = """
    * Defining a word/phrase meaning, typically using a child-friendly definition. 
    * Defining a character/object as belonging to a higher category 
    * Discussing the function or purpose of an object is coded here. 
    * Vocabulary elaborations contextualize the focal word, but still provide rich information about the word’s meaning or contexts in which it is used
    * Using examples/non-examples to elaborate on a vocabulary word’s meaning is a vocabulary elaboration  
    * Clarifying a more specific/precise name for something supports vocabulary precision
    * Referencing other dialects or languages can be used to support vocabulary development
    * Use context to infer whether a vague teacher question is referencing a vocabulary definition or a simpler descriptive request 
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_making_connections(self, utterance):
        code_name = "Making Connections"
        code_definition = "Involves modeling the implicit link or explicit comparison between text and personal experiences."
        keywords = """
    Key phrases: Have you ever…?, Remember when we…?, This is like when we…., This reminds me of my/our….
    Possible keywords: Last night, yesterday, tomorrow, later, might, plan to, remember when, do you recall?
    """
        code_notes = """
    * Link to children’s or teacher’s personal experiences/events in the past, present, or future.
    * Expresses possibility for future events of teacher/children (which is distinct from predictions about future text events because personal in nature) 
    * This code includes connections to other books, media, or cultural products that are directly experienced by the teacher or children
    * This code includes connections to the classroom/school’s  theme/unit of study in past/present/future
    * Hypothetical statements are not coded. 
    * When a making connection episode begins, you may code several utterances as making a connection even though that standalone utterance would not be coded.
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

    def code_building_knowledge(self, utterance):
        code_name = "Building Knowledge"
        code_definition = (
            "This code involves building background information and facts."
        )
        keywords = """
    Key phrase: What do you know about…?
    """
        code_notes = """
    * Providing or requesting background information/facts beyond that in text and that include scientific, historic or other objective facts (not judgments). 
    * References factual information that goes beyond what is explicitly stated in the text 
    * Building knowledge references need not be tightly linked to the text
    * Discussing dialect/translations always references background knowledge about language.
    * This code can include references to general factual talk that is impersonal, but goes beyond the text to build background knowledge.
    """
        example = ""

        code_response, explanation = self.generate_code(
            utterance, code_name, keywords, code_definition, code_notes, example
        )
        return code_response, explanation  # Returning both code and explanation

class RuleBasedQuestionGenerator:
    """Generates questions using a rule-based approach.

    This class implements a set of rules to transform declarative sentences into questions.
    """

    def __init__(self):
        """Initializes the RuleBasedQuestionGenerator.

        Currently, no specific initialization is required.
        """
        pass

    def generate_question(self, sentence):
        """Generates a question from the given sentence.

        Args:
            sentence (str): The input sentence.

        Returns:
            str: The generated question.
        """
        # Implement rule-based question generation logic here
        # This is a placeholder; replace with actual rules
        if sentence.endswith('.'):
          return "Is this a fact?"
        return "What about this?"
import unittest
from src.rule_based_question_generator import RuleBasedQuestionGenerator

class TestRuleBasedQuestionGenerator(unittest.TestCase):
    """Unit tests for the RuleBasedQuestionGenerator class.

    This class contains test methods to verify the functionality of the RuleBasedQuestionGenerator.
    """

    def test_generate_question(self):
        """Tests the generate_question method.

        Checks if the question generation method returns a string.
        """
        generator = RuleBasedQuestionGenerator()
        question = generator.generate_question('This is a sentence.')
        self.assertIsInstance(question, str)
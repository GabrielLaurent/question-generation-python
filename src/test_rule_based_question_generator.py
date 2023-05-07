import unittest
from src.rule_based_question_generator import RuleBasedQuestionGenerator

class TestRuleBasedQuestionGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = RuleBasedQuestionGenerator()

    def test_generate_question(self):
        context = "The Eiffel Tower is located in Paris."
        answer = "Paris"
        question = self.generator.generate_question(context, answer)
        self.assertIsNotNone(question)
        self.assertTrue(isinstance(question, str))

    def test_generate_question_empty_context(self):
        context = ""
        answer = "Paris"
        question = self.generator.generate_question(context, answer)
        self.assertIsNone(question)
    
    def test_generate_question_empty_answer(self):
        context = "The Eiffel Tower is located in Paris."
        answer = ""
        question = self.generator.generate_question(context, answer)
        self.assertIsNone(question)
import unittest
from src.rule_based_question_generator import RuleBasedQuestionGenerator

class TestRuleBasedQuestionGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = RuleBasedQuestionGenerator()

    def test_generate_question(self):
        context = "The capital of France is Paris."
        answer = "Paris"
        question = self.generator.generate_question(context, answer)
        self.assertEqual(question, "What is Paris?")

    def test_generate_questions_for_example(self):
        context = "The sky is blue and the grass is green."
        answers = ["blue", "green"]
        questions = self.generator.generate_questions_for_example(context, answers)
        self.assertEqual(len(questions), 2)
        self.assertEqual(questions[0], "What is blue?")
        self.assertEqual(questions[1], "What is green?")

if __name__ == '__main__':
    unittest.main()

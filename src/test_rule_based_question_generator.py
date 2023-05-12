import unittest
from src.rule_based_question_generator import RuleBasedQuestionGenerator

class TestRuleBasedQuestionGenerator(unittest.TestCase):

    def setUp(self):
        self.question_generator = RuleBasedQuestionGenerator()

    def test_generate_question_simple(self):
        context = "The cat sat on the mat."
        answer = "cat"
        expected_question = "What sat on the mat?"
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

    def test_generate_question_with_location(self):
        context = "Paris is the capital of France."
        answer = "Paris"
        expected_question = "What is the capital of France?"
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

    def test_generate_question_with_date(self):
        context = "The battle of Hastings was in 1066."
        answer = "1066"
        expected_question = "When was the battle of Hastings?"
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

    def test_generate_question_with_who(self):
        context = "Alice lives in Wonderland."
        answer = "Alice"
        expected_question = "Who lives in Wonderland?"
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

    def test_generate_question_with_no_matching_rule(self):
        context = "This is a test sentence."
        answer = "sentence"
        expected_question = None  # Or a default question if the rule-based generator provides one
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

    def test_generate_question_numeric(self):
        context = "The answer is 42."
        answer = "42"
        expected_question = "What is the answer?"
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

    def test_generate_question_multiple_words(self):
        context = "The quick brown fox jumps over the lazy dog."
        answer = "quick brown fox"
        expected_question = "What jumps over the lazy dog?"
        generated_question = self.question_generator.generate_question(context, answer)
        self.assertEqual(generated_question, expected_question)

if __name__ == '__main__':
    unittest.main()

import unittest
from src.rule_based_question_generator import generate_question

class TestRuleBasedQuestionGenerator(unittest.TestCase):

    def test_generate_question_with_entities(self):
        text = "Barack Obama was the 44th President of the United States."
        questions = generate_question(text)
        self.assertEqual(questions, ['What is Barack?', 'What is Obama?', 'What is President?', 'What is States.'])

    def test_generate_question_without_entities(self):
        text = "this is a sentence without proper nouns."
        questions = generate_question(text)
        self.assertEqual(questions, [])

    def test_generate_question_with_empty_string(self):
        text = ""
        questions = generate_question(text)
        self.assertEqual(questions, [])

if __name__ == '__main__':
    unittest.main()
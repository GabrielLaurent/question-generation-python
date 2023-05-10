import unittest
from src.evaluation import calculate_bleu

class TestEvaluation(unittest.TestCase):

    def test_calculate_bleu_with_valid_input(self):
        generated_questions = ["What is the capital of France?", "Who wrote Hamlet?"]
        reference_answers = ["Paris is the capital of France.", "William Shakespeare wrote Hamlet."]
        bleu_score = calculate_bleu(generated_questions, reference_answers)
        self.assertIsInstance(bleu_score, float)
        self.assertTrue(0.0 <= bleu_score <= 1.0)

    def test_calculate_bleu_with_empty_questions(self):
        generated_questions = []
        reference_answers = ["Paris is the capital of France.", "William Shakespeare wrote Hamlet."]
        bleu_score = calculate_bleu(generated_questions, reference_answers)
        self.assertEqual(bleu_score, 0.0)

    def test_calculate_bleu_with_empty_answers(self):
        generated_questions = ["What is the capital of France?", "Who wrote Hamlet?"]
        reference_answers = []
        bleu_score = calculate_bleu(generated_questions, reference_answers)
        self.assertEqual(bleu_score, 0.0)

    def test_calculate_bleu_with_no_common_words(self):
        generated_questions = ["apple banana orange", "grape kiwi"] #No common words with answers below
        reference_answers = ["Paris is the capital of France.", "William Shakespeare wrote Hamlet."]
        bleu_score = calculate_bleu(generated_questions, reference_answers)
        self.assertIsInstance(bleu_score, float)
        self.assertTrue(0.0 <= bleu_score <= 1.0)

    def test_calculate_bleu_with_empty_reference_sentence(self):
        generated_questions = ["What is the capital of France?", "Who wrote Hamlet?"]
        reference_answers = ["", ""] #Empty strings
        bleu_score = calculate_bleu(generated_questions, reference_answers)
        self.assertIsInstance(bleu_score, float)
        self.assertTrue(0.0 <= bleu_score <= 1.0)

if __name__ == '__main__':
    unittest.main()
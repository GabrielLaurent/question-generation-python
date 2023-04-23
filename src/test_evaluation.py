import unittest
from src.evaluation import Evaluator

class TestEvaluator(unittest.TestCase):
    """Unit tests for the Evaluator class.

    This class contains test methods to verify the functionality of the Evaluator.
    """

    def test_calculate_bleu(self):
        """Tests the calculate_bleu method.

        Checks if the BLEU score calculation returns a float value.
        """
        evaluator = Evaluator()
        bleu_score = evaluator.calculate_bleu('candidate sentence', 'reference sentence')
        self.assertIsInstance(bleu_score, float)

    def test_calculate_rouge(self):
        """Tests the calculate_rouge method.

        Checks if the ROUGE score calculation returns a float value.
        """
        evaluator = Evaluator()
        rouge_score = evaluator.calculate_rouge('candidate sentence', 'reference sentence')
        self.assertIsInstance(rouge_score, float)
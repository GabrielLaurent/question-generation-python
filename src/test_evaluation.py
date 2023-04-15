import unittest
from src.evaluation import calculate_eval_metrics

class TestEvaluation(unittest.TestCase):

    def test_calculate_eval_metrics_empty_data(self):
        gold_data = []
        generated_data = []
        metrics = calculate_eval_metrics(gold_data, generated_data)
        self.assertEqual(metrics['exact_match'], 0.0)
        self.assertEqual(metrics['f1_score'], 0.0)

    def test_calculate_eval_metrics_rule_based(self):
        gold_data = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Who wrote Hamlet?", "answer": "Shakespeare"}
        ]
        generated_data = [
            {"question": "What is Paris?", "answer": "Paris"},
            {"question": "Who wrote Hamlet?", "answer": "Shakespeare"}
        ]
        metrics = calculate_eval_metrics(gold_data, generated_data)
        self.assertAlmostEqual(metrics['exact_match'], 0.5)
        self.assertAlmostEqual(metrics['f1_score'], 0.75)

    def test_calculate_eval_metrics_transformer(self):
        gold_data = [
            {"question": "What is the capital of France?", "answer": "Paris"},
            {"question": "Who wrote Hamlet?", "answer": "Shakespeare"}
        ]
        generated_data = [
            {"question": "What city is the capital of France?", "answer": "Paris"},
            {"question": "Who is the writer of Hamlet?", "answer": "Shakespeare"}
        ]
        metrics = calculate_eval_metrics(gold_data, generated_data)
        self.assertAlmostEqual(metrics['exact_match'], 0.5)
        self.assertAlmostEqual(metrics['f1_score'], 0.75) #same as rule_based for demo
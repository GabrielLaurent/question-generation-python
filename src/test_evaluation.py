import unittest
from src.evaluation import evaluate_question

class TestEvaluation(unittest.TestCase):

    def test_evaluate_question_with_perfect_match(self):
        generated_question = "What is the capital of France?"
        reference_question = "What is the capital of France?"
        score = evaluate_question(generated_question, reference_question)
        self.assertEqual(score, 1.0)

    def test_evaluate_question_with_partial_match(self):
        generated_question = "Capital of France?"
        reference_question = "What is the capital of France?"
        score = evaluate_question(generated_question, reference_question)
        self.assertGreater(score, 0.0)
        self.assertLess(score, 1.0)

    def test_evaluate_question_with_no_match(self):
        generated_question = "What is the capital of Germany?"
        reference_question = "What is the capital of France?"
        score = evaluate_question(generated_question, reference_question)
        self.assertEqual(score, 0.0)

    def test_evaluate_on_dummy_dataset(self):
        # Dummy dataset
        dummy_data = [
            {"generated_question": "What is the capital of France?", "reference_question": "What is the capital of France?"},
            {"generated_question": "Capital of Germany?", "reference_question": "What is the capital of Germany?"},
            {"generated_question": "President of USA?", "reference_question": "Who is the President of the United States?"},
            {"generated_question": "Random question", "reference_question": "Irrelevant question"}
        ]
        
        total_score = 0.0
        for data_point in dummy_data:
            total_score += evaluate_question(data_point["generated_question"], data_point["reference_question"])
        
        average_score = total_score / len(dummy_data)
        print(f"Average score on dummy dataset: {average_score}")
        self.assertGreaterEqual(average_score, 0.0)
        self.assertLessEqual(average_score, 1.0)
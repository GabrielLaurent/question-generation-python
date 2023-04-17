import unittest
from src.rule_based_question_generator import RuleBasedQuestionGenerator
from src.question_type_classifier import QuestionTypeClassifier

class TestRuleBasedQuestionGenerator(unittest.TestCase):

    def setUp(self):
        # Train a question type classifier for testing
        self.classifier = QuestionTypeClassifier()
        contexts = ["The sky is blue", "The grass is green", "Water is wet"]
        question_types = ["Simple", "Simple", "Complex"]
        self.classifier.train(contexts, question_types)
        self.classifier.save()
        self.generator = RuleBasedQuestionGenerator()

    def test_generate_question_simple(self):
        context = "The sky is blue."
        answer = "blue"
        question, success = self.generator.generate_question(context, answer)
        self.assertTrue(success)
        self.assertIn("What about", question)

    def test_generate_question_complex(self):
        context = "Water is wet, and this is important for life."
        answer = "wet"
        question, success = self.generator.generate_question(context, answer)
        self.assertTrue(success)
        self.assertIn("Considering", question)

    def test_no_classifier(self):
        # Temporarily disable the classifier by setting it to None.
        # Then question generation will return a default question
        self.generator.question_type_classifier = None
        context = "Water is wet, and this is important for life."
        answer = "wet"
        question, success = self.generator.generate_question(context, answer)
        self.assertFalse(success)
        self.assertIn("disabled", question)

    def tearDown(self):
        # Clean up the trained model file
        import os
        try:
            os.remove('question_type_model.joblib')
        except FileNotFoundError:
            pass

if __name__ == '__main__':
    unittest.main()

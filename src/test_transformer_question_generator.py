import unittest
from src.transformer_question_generator import TransformerQuestionGenerator
import json
import os

class TestTransformerQuestionGenerator(unittest.TestCase):

    def setUp(self):
        self.tqg = TransformerQuestionGenerator(epochs=1) # Reduced epochs for speed
        self.sample_data = self.tqg.load_data()
        self.context = self.sample_data[0]['context']
        self.answer = self.sample_data[0]['answer']
        self.output_dir = self.tqg.output_dir

    def test_train(self):
        self.tqg.train()
        self.assertTrue(os.path.exists(self.output_dir), "Training output directory not created.")
        # Basic check if model files exist.  More sophisticated checks could be added.
        model_files = [f for f in os.listdir(self.output_dir) if 'pytorch_model.bin' in f]
        self.assertTrue(len(model_files) > 0, "Model files not saved.")

    def test_generate_question(self):
        # First train, then generate.
        self.tqg.train()
        question = self.tqg.generate_question(self.context, self.answer)
        self.assertIsInstance(question, str)
        self.assertTrue(len(question) > 0)

    def tearDown(self):
        # Clean up the output directory after the test.
        import shutil
        if os.path.exists(self.output_dir):
            shutil.rmtree(self.output_dir)

if __name__ == '__main__':
    unittest.main()
import unittest
import json
import os
from src.data_loader import load_data

class TestDataLoader(unittest.TestCase):

    def setUp(self):
        # Create a sample data file for testing
        self.sample_data = [
            {
                "context": "This is a sample context.",
                "question": "What is this?",
                "answer": "A sample."
            },
            {
                "context": "Another sample context here.",
                "question": "What about this one?",
                "answer": "Another sample."
            }
        ]
        self.sample_file_path = "sample_data.json"
        with open(self.sample_file_path, 'w') as f:
            json.dump(self.sample_data, f)

    def tearDown(self):
        # Clean up the sample data file after testing
        os.remove(self.sample_file_path)

    def test_load_data_type(self):
        data = load_data(self.sample_file_path)
        self.assertIsInstance(data, list)

    def test_load_data_shape(self):
        data = load_data(self.sample_file_path)
        self.assertEqual(len(data), len(self.sample_data))

    def test_load_data_content(self):
        data = load_data(self.sample_file_path)
        self.assertEqual(data, self.sample_data)

    def test_load_data_empty_file(self):
        empty_file_path = "empty_data.json"
        open(empty_file_path, 'w').close()
        data = load_data(empty_file_path)
        self.assertEqual(data, [])
        os.remove(empty_file_path)


if __name__ == '__main__':
    unittest.main()
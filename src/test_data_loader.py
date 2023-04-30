import unittest
import os
import json
from unittest.mock import patch
import logging
from io import StringIO

from src.data_loader import DataLoader
from src.logger import setup_logger


class TestDataLoader(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_data.json'
        self.logger = setup_logger(__name__, level=logging.DEBUG) # Setting level to DEBUG
        self.log_stream = StringIO()
        handler = logging.StreamHandler(self.log_stream)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        with open(self.test_file, 'w') as f:
            json.dump([{"context": "test context", "answer": "test answer"}], f)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
            handler.close()

    def test_load_data_success(self):
        data_loader = DataLoader(self.test_file)
        data = data_loader.load_data()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['context'], 'test context')
        self.assertIn('Successfully loaded data', self.log_stream.getvalue())

    def test_load_data_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            data_loader = DataLoader('non_existent_file.json')
            data_loader.load_data()
        self.assertIn('File not found', self.log_stream.getvalue())

    def test_load_data_json_decode_error(self):
        with open(self.test_file, 'w') as f:
            f.write('invalid json')
        
        data_loader = DataLoader(self.test_file)
        with self.assertRaises(json.JSONDecodeError):
            data_loader.load_data()

        self.assertIn('Error decoding JSON', self.log_stream.getvalue())

if __name__ == '__main__':
    unittest.main()
import unittest
from src.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):
    """Unit tests for the DataLoader class.

    This class contains test methods to verify the functionality of the DataLoader.
    """

    def test_load_data_valid(self):
        """Tests loading data from a valid JSON file.

        Checks if the data is loaded correctly when the JSON file exists and is properly formatted.
        """
        loader = DataLoader('data/sample.json')
        data = loader.load_data()
        self.assertIsInstance(data, list)

    def test_load_data_invalid_file(self):
        """Tests loading data from a non-existent JSON file.

        Checks if the function handles the case where the JSON file does not exist.
        """
        loader = DataLoader('nonexistent_file.json')
        data = loader.load_data()
        self.assertEqual(data, [])

    def test_load_data_invalid_json(self):
        """Tests loading data from a JSON file with invalid format.

        Checks if the function handles the case where the JSON file contains invalid JSON.
        """
        # Create a temporary file with invalid JSON
        with open('invalid.json', 'w') as f:
            f.write('{"invalid": "json"')

        loader = DataLoader('invalid.json')
        data = loader.load_data()
        self.assertEqual(data, [])
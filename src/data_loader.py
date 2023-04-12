import json
from src.logger import logger
from src.mlflow_utils import log_param, log_metric

class DataLoader:
    def __init__(self, file_path='data/sample.json'):
        self.file_path = file_path
        self.data = self.load_data()
        logger.info(f'Loaded data from {file_path}')

    def load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            logger.error(f'File not found: {self.file_path}')
            return []
        except json.JSONDecodeError:
            logger.error(f'Invalid JSON format in: {self.file_path}')
            return []

    def get_examples(self, num_examples=None):
        if num_examples is None:
            return self.data
        else:
            return self.data[:num_examples]


if __name__ == '__main__':
    # Example usage
    loader = DataLoader()
    examples = loader.get_examples(num_examples=2)
    print(examples)

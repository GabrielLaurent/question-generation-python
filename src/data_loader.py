import json
from src.logger import setup_logger

logger = setup_logger(__name__)

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        logger.info(f'Initializing DataLoader with file: {file_path}')

    def load_data(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
            logger.info(f'Successfully loaded data from {self.file_path}')
            return data
        except FileNotFoundError as e:
            logger.error(f'File not found: {self.file_path}', exc_info=True)
            raise e
        except json.JSONDecodeError as e:
            logger.error(f'Error decoding JSON from {self.file_path}', exc_info=True)
            raise e
        except Exception as e:
            logger.exception(f'An unexpected error occurred during data loading')
            raise e

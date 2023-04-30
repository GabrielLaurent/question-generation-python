import logging
import os

LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):  # Create log directory if absent
    os.makedirs(LOG_DIR)

LOG_FILE = os.path.join(LOG_DIR, 'question_generation.log')

def setup_logger(name, log_file=LOG_FILE, level=logging.INFO):
    """To setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    # Corrected logging format and added datefmt for clarity
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# Example usage (this won't run when the file is imported,
# but demonstrates how to get a logger in other modules).
if __name__ == '__main__':
    logger = setup_logger('main_app')
    logger.info('This is a test log message.')
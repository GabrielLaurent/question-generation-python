import logging

def setup_logger(name, log_file, level=logging.INFO):
    """Sets up a logger to write to a file.

    Args:
        name (str): The name of the logger.
        log_file (str): The path to the log file.
        level (int): The logging level (e.g., logging.INFO, logging.DEBUG).

    Returns:
        logging.Logger: The configured logger object.
    """
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
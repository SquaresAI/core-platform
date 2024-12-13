# Helper Functions

import os
import logging

def setup_logger(name: str, log_file: str, level=logging.INFO) -> logging.Logger:
    """Sets up and returns a logger instance."""
    handler = logging.FileHandler(log_file)
    handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s'))

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

def ensure_directory(path: str):
    """Ensures that a directory exists, creating it if necessary."""
    if not os.path.exists(path):
        os.makedirs(path)

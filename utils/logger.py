"""Configure the global logger for the test framework."""

import logging
import sys


def setup_logger(name: str = "swag_labs", level: str = "INFO") -> logging.Logger:
    """Creates and configure logger"""
    logger = logging.getLogger(name)
    numeric_level = getattr(logging, level.upper(), logging.INFO)

    if not logger.handlers:
        logger.setLevel(numeric_level)

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-7s | %(name)s | %(message)s",
            datefmt="%H:%M:%S",
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    else:
        logger.setLevel(numeric_level)

    return logger

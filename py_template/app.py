"""
Module: app.py

Main application logic.
"""

from loguru import logger

from py_template.core import foo

# Automatically updated by "poetry-dynamic-versioning"
__version__ = "0.0.0"


def run() -> None:
    """
    Run the application.
    """
    logger.info("Hello world!")
    logger.info(f"App Version: {__version__}")
    logger.info(f"foo.bar() returned {foo.bar()}")

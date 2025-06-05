"""
Module: app.py

Main application logic.
"""

from loguru import logger

from py_template.core import foo


def run() -> None:
    """
    Run the application.
    """
    logger.info("Hello world!")
    logger.info(f"foo.bar() returned {foo.bar()}")

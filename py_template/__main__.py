"""
Module: __main__.py

Boilerplate module to run the application.

You can run this module via the following methods:
- Entry point (after installation, recommended): `py-template`
- Module: `python3 -m py_template`
"""

from loguru import logger

from py_template import app


@logger.catch  # Add pretty exceptions
def main() -> None:
    """
    Entry-point of the application.
    """
    app.run()


# The entry point in `pyproject.toml` will call `main()` directly, this is only for running as a script/module
if __name__ == "__main__":
    main()

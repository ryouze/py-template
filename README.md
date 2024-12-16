```
This is a barebones Python project template.

Features:
- Poetry for dependencies, pytest for testing.
- CI with GitHub Actions.
- Unlicense for unrestricted use.

You can find the sample README below. Feel free to modify it to suit your project.

Note: The MIT license is referenced, but this repo is actually under the Unlicense. I license most of my projects under MIT, so I put it in the template.
```


# py-template

[![CI](https://github.com/ryouze/py-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ryouze/py-template/actions/workflows/ci.yml)

py-template is a barebones Python project template.


## Motivation

Text here.


## Features

- Written in modern Python (Python 3.11+).
- Comprehensive documentation with docstrings.
- Strict static typing.


## Tested Systems

This project has been tested on the following systems:

- macOS 15.1 (Sequoia)
<!-- - Manjaro 24.0 (Wynsdey)
- Windows 11 23H2 -->

Automated testing is also performed on the latest version of GNU/Linux (Python 3.11-3.13) using GitHub Actions.


## Requirements

To run this project, you'll need:

- Python 3.11 or higher
- [Poetry](https://python-poetry.org/) (optional for users, required for developers)


## Setup

Follow these steps to set up the project:

1. **Clone the repository**:

    ```sh
    git clone https://github.com/ryouze/py-template.git
    ```

2. **Install the project**:

    ```sh
    cd py-template
    ```

    **Option 1: Poetry (recommended)**:

    ```sh
    poetry install --without dev
    poetry shell
    ```

    **Option 2: Pip (if you don't want to use 3rd-party build tools)**:

    ```sh
    python3 -m venv .env
    source .env/bin/activate
    pip install .
    ```

    **Note:** This installs only production dependencies (i.e., for regular users). To install development dependencies, refer to the [Development and Testing](#development-and-testing) section.


## Usage

**Note:** You must activate the virtual environment (`poetry shell` or `source .env/bin/activate`) every time you open a new terminal. Most IDEs can activate the venv automatically (VSCode: `python.terminal.activateEnvInCurrentTerminal`).

To run the program, use the following command:

```sh
py-template
```


## Development and Testing

The `--without dev` flag in `poetry install` skips the installation of dev dependencies like `pytest`.

To install all dependencies (including development), use:

```sh
poetry install
```

To run tests manually, activate the virtual environment and run:

```sh
pytest -v
```

**Note:** Installing the dev dependencies using pip is not supported due to syntax differences in the `pyproject.toml` file. However, if you insist on using pip, you can install the project in [editable mode](https://pip.pypa.io/en/stable/topics/local-project-installs/) (`pip install -e .`) and then manually install the dev dependencies under `[tool.poetry.group.dev.dependencies]` in `pyproject.toml`.


## Credits

- [loguru](https://github.com/Delgan/loguru)
- [pytest](https://github.com/pytest-dev/pytest)


## Contributing

All contributions are welcome.


## License

This project is licensed under the MIT License.

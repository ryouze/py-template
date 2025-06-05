> ## About this template
>
> Minimal Python project template built around Poetry.
> Features:
> * Poetry for dependency management, pytest for testing.
> * CI pipeline on GitHub Actions.
> * Unlicense by default for unrestricted reuse.
>
> Clone it, rename it, pick a license, and start coding. Follow the steps below, then delete this block.
>
> ### 1. Pick a license
>
> The repo ships with the Unlicense, but the text mentions MIT because most of my own projects use MIT.
> Replace the `LICENSE` file with MIT, Apache-2.0, BSD-3, or any other license you prefer.
>
> ### 2. Pick a project name
>
> Choose two forms of the name:
> * `your_project`  – import/package name
> * `your-project`  – distribution name
>
> Replace every placeholder:
> * Rename directory `py_template/` to `your_project/`.
> * Search-replace `py_template` -> `your_project`.
> * Search-replace `py-template` -> `your-project`.
>
> ### 3. Update metadata
>
> Edit `pyproject.toml` and change the following fields:
> * `description` - same slogan as in the README.
> * `authors` -  name & e-mail.
> * `license` - keep `license = { file = "LICENSE" }`, or replace with `license = "MIT"` (or another SPDX identifier) for clean PyPI classification


# py-template

[![CI](https://github.com/ryouze/py-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ryouze/py-template/actions/workflows/ci.yml)
[![Release](https://github.com/ryouze/py-template/actions/workflows/release.yml/badge.svg)](https://github.com/ryouze/py-template/actions/workflows/release.yml)
![Release version](https://img.shields.io/github/v/release/ryouze/py-template)

py-template is a barebones Python project template.


## Motivation

Text here.


## Features

- Written in modern Python (Python 3.12+).
- Comprehensive documentation with docstrings.
- Strict static typing.


## Tested Systems

This project has been tested on the following systems:

- macOS 15.3 (Sequoia)
<!-- - Manjaro 24.0 (Wynsdey)
- Windows 11 23H2 -->

Automated testing is also performed on the latest version of GNU/Linux (Python 3.12-3.13) using GitHub Actions.


## Requirements

To run this project, you'll need:

- Python 3.12 or higher
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

    To install only the production dependencies (i.e., for regular users), choose one of the following options:

    **Option 1: [Poetry](https://python-poetry.org/) (recommended)**:

    <!--
    Groups:
    * '--without dev' installs every non-optional group except 'dev'.
    * '--only main' installs nothing except the implicit main group, so it will silently drop any future non-dev groups you might add (e.g., 'docs' or 'bench').
    The Poetry maintainers recommend '--without dev' for a production install and '--only main' only when you know you want to strip out everything but the runtime set. However, since we set the 'dev' group as optional, 'poetry install' will only install the production dependencies by default, so you can skip the '--without dev' flag.
    Virtual-environment activation:
    The old 'poetry shell' command moved to a plugin. Thus, 'poetry env' activate is now the built-in way to enter the venv; it only prints the shell command.
    Use 'eval $(poetry env activate)' for Bourne-like shells, 'eval (poetry env activate)' for Fish and 'Invoke-Expression (poetry env activate)' for PowerShell.
    -->

    ```sh
    poetry install
    eval $(poetry env activate)
    ```

    **Option 2: Pip in [editable mode](https://pip.pypa.io/en/stable/topics/local-project-installs/) (if you don't want to use 3rd-party build tools)**:

    ```sh
    python3 -m venv .env
    source .env/bin/activate
    pip install -e .
    ```

    Alternatively, the `generate_requirements.py` script can be used to generate `requirements.txt` for the traditional `pip install -r requirements.txt` method. Compatibility with this method is not guaranteed, as the project uses `poetry` for dependency management.

    ```sh
    python3 generate_requirements.py
    pip install -r requirements.txt
    ```

    **Note:** To install development dependencies as well, refer to the [Development and Testing](#development-and-testing) section.


## Usage

> [!IMPORTANT]
> You must activate the virtual environment (`eval $(poetry env activate)` or `source .env/bin/activate`) every time you open a new terminal. Most IDEs can activate the venv automatically (VSCode: `python.terminal.activateEnvInCurrentTerminal`).

To run the program, use the following command:

```sh
py-template
```


## Development and Testing

The `poetry install` skips the installation of dev dependencies (e.g., `pytest`), because they're marked as `optional = true`.

To install all dependencies (including development), use:

```sh
poetry install --all-groups
```

Or `poetry install --with dev` to install only the `dev` group, but the `--all-groups` option is recommended to ensure all non-production dependencies are installed.

To run tests manually, activate the virtual environment and run:

```sh
pytest -v
```

> [!NOTE]
> Installing the dev dependencies using pip is not supported due to syntax differences in the `pyproject.toml` file. However, if you insist on using pip, you can manually install the packages listed under `[tool.poetry.group.dev.dependencies]`.


## Credits

- [loguru](https://github.com/Delgan/loguru)
- [pytest](https://github.com/pytest-dev/pytest)


## Contributing

All contributions are welcome.


## License

This project is licensed under the MIT License.

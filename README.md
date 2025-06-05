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
> * `your_project` - import/package name
> * `your-project` - distribution name
>
> Replace every placeholder:
> * Rename directory `py_template/` to `your_project/`.
> * Search-replace `py_template` -> `your_project`.
> * Search-replace `py-template` -> `your-project`.
> > * Search-replace `ryouze` -> `your_github_username`.
>
> ### 3. Update metadata
>
> Edit `pyproject.toml` and change the following fields:
> * `license` - your license.
> * `description` - same slogan as in the README.
> * `authors` - name & e-mail.
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


## Pre-built Wheels

Pre-built wheels `(*.whl`) are available. You can install the latest version from the [Releases](../../releases) page using [pipx](https://github.com/pypa/pipx):

```sh
pipx install https://github.com/ryouze/py-template/releases/latest/download/py_template-latest-py3-none-any.whl
```

This is the recommended choice for users who just want to run the app. Only the required dependencies will be installed, and the app will be available globally in any directory as `py-template`.

If that doesn't work, you can install it from the latest source code (slower, not recommended), try the following:

```sh
pipx install git+https://github.com/ryouze/py-template.git
```

> [!NOTE]
> This won't set the `__version__` to the latest release because `poetry-dynamic-versioning` runs on `poetry build`; you'll get the fallback version from `pyproject.toml` instead.

If you want to update to the latest version, please note that the app is not on PyPI, so you cannot use `pipx upgrade`. Instead, you can uninstall the current version and install the latest one again:

```sh
pipx uninstall py-template
pipx install https://github.com/ryouze/py-template/releases/latest/download/py_template-latest-py3-none-any.whl
```

Once installed, refer to the [Usage](#usage) section for further instructions.


## Requirements

To run this project, you'll need:

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/) (optional for users, required for developers)


## Setup

> [!NOTE]
> For users who *just want to run the app*, using `pipx` is recommended (see the [Pre-built Wheels](#pre-built-wheels) section).

Follow these steps to set up the project:

1. **Clone the repository**:

    ```sh
    git clone https://github.com/ryouze/py-template.git
    ```

2. **Install the project**:

    ```sh
    cd py-template
    ```

    **Option 1 - Poetry**:

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
    ```

    **Option 2 - pip in editable mode**:

    ```sh
    python3 -m venv .env
    source .env/bin/activate
    pip install -e .
    ```

    This will only install the production dependencies. To install the development dependencies as well, refer to the [Development and Testing](#development-and-testing) section.


## Usage

**a) If installed with pipx, you can run the app from any directory**:

```sh
py-template
```

**b) If installed with Poetry, you don't need to activate the virtual environment, instead, simply run this from the project directory**:

```sh
poetry run py-template
```

The `eval $(poetry env activate)` is still available, though, to activate the virtual environment manually if needed.

**c) If you're using `pip` in editable mode, you need to activate the virtual environment first**:

```sh
source .env/bin/activate
```

Or enable the virtual environment automatically in your terminal or IDE settings. For example, in VSCode, you can set the `python.terminal.activateEnvInCurrentTerminal` setting to `true`.

Then you can run the command directly:

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


## Credits

- [loguru](https://github.com/Delgan/loguru)
- [pytest](https://github.com/pytest-dev/pytest)


## Contributing

All contributions are welcome.


## License

This project is licensed under the MIT License.

> ## About this template
>
> A minimal Python project template built around Poetry.
>
> Features:
>
> * Poetry for dependency management, and pytest for testing.
> * CI pipeline using GitHub Actions.
> * Unlicense by default for unrestricted reuse (no attribution required).
>
> Follow these steps to set it up for your own project.
>
> ### 1. Choose a license
>
> Tip: The repository uses the Unlicense by default, but the text mentions MIT because most of my projects use MIT.
> Replace the `LICENSE` file (at the root of this repository) with MIT, Apache-2.0, BSD-3, or any other license you prefer.
>
> ### 2. Choose a project name
>
> You’ll need two forms of the project name:
>
> * `your_project` - the import/package name
> * `your-project` - the distribution name
>
> Replace the following placeholders:
>
> * Rename the `py_template/` directory to `your_project/` (at the root of this repository).
> * Search and replace `py_template` with `your_project` (in all files).
> * Search and replace `py-template` with `your-project` (in all files).
> * Search and replace `ryouze` with your GitHub username (in all files).
>
> ### 3. Update metadata
>
> Edit `pyproject.toml` and update the following fields:
>
> * `license` - your chosen license.
> * `description` - same short description as in the README.
> * `authors` - your name and email.
> * `license` - keep `license = { file = "LICENSE" }`, or use `license = "MIT"` (or another SPDX identifier) for cleaner PyPI classification.
>
> ### 4. Remove unnecessary files
>
> Delete `poetry.lock` so that it gets regenerated with your dependencies on the next `poetry install`.
> Also remove this section from the README.
>
> ### 5. Bumping the version
>
> Use `bump_version.sh` to bump the version number in `pyproject.toml` and create a Git tag.


# py-template

[![CI](https://github.com/ryouze/py-template/actions/workflows/ci.yml/badge.svg)](https://github.com/ryouze/py-template/actions/workflows/ci.yml)

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
- [Poetry](https://python-poetry.org/) (optional and only for developers)


## Setup

### Pipx (Recommended for Users)

If you just want to run the app, the recommended method is to install it with [pipx](https://github.com/pypa/pipx). This allows you to run the app from any directory, enables easy updates, and keeps it isolated from other Python packages. Poetry is *not* required for this installation method.

To install the app with `pipx`, run:

```sh
pipx install git+https://github.com/ryouze/py-template.git
```

To update to the latest version, run:

```sh
pipx upgrade py-template
```

Once installed, refer to the [Usage](#usage) section.


### Poetry or pip (Recommended for Developers)

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

    This installs only the production dependencies. To install development dependencies as well, see the [Development and Testing](#development-and-testing) section.


## Usage

**a) If installed via pipx, you can run the app from any directory**:

```sh
py-template
```

**b) If installed via Poetry, there's no need to activate the virtual environment. Simply run this from the project directory**:

```sh
poetry run py-template
```

You can still manually activate the virtual environment using `eval $(poetry env activate)` if needed.

**c) If installed via pip in editable mode, activate the virtual environment first**:

```sh
source .env/bin/activate
```

Or configure your terminal or IDE to automatically activate the virtual environment. For example, in VSCode, set `python.terminal.activateEnvInCurrentTerminal` to `true`.

Then you can run the command directly:

```sh
py-template
```


## Development and Testing

By default, `poetry install` skips dev dependencies (e.g., `pytest`) because they're marked as `optional = true`.

To install all dependencies, including development ones, run:

```sh
poetry install --all-groups
```

Or `poetry install --with dev` to install only the `dev` group, but the `--all-groups` option is recommended to ensure all non-production dependencies are installed.

To run tests manually, use:

```sh
poetry run pytest -v
```


## Credits

- [loguru](https://github.com/Delgan/loguru)
- [pytest](https://github.com/pytest-dev/pytest)


## Contributing

All contributions are welcome.


## License

This project is licensed under the MIT License.

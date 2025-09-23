<article>
# uv Quick Reference

This reference provides essential uv commands organized by workflow. For comprehensive documentation, visit the [uv docs](https://docs.astral.sh/uv/). Need help getting started? Check out [how to install uv](https://pydevtools.com/handbook/how-to/how-to-install-uv/) and [create your first Python project](https://pydevtools.com/handbook/tutorial/create-your-first-python-project/).

## Project Creation

| Command | Description |
|---------|-------------|
| `uv init` | Initialize project in current directory |
| `uv init myproject` | Create new project directory |
| `uv init --lib` | Initialize library project |
| `uv init --app` | Initialize application project |
| `uv init --python 3.12` | Specify Python version |

## Dependency Management

| Command | Description |
|---------|-------------|
| `uv add requests` | Add production dependency |
| `uv add --dev pytest` | Add development dependency |
| `uv add -r requirements.txt` | Import from requirements file ([migration guide](https://pydevtools.com/handbook/how-to/migrate-requirements.txt/)) |
| `uv remove requests` | Remove dependency |
| `uv sync` | Install dependencies from lockfile |
| `uv lock` | Update lockfile |
| `uv lock --upgrade` | Upgrade all dependencies |
| `uv tree` | View dependency tree |

## Script Management

| Command | Description |
|---------|-------------|
| `uv init --script myscript.py` | Create script with metadata |
| `uv add click --script myscript.py` | Add script dependency |
| `uv run myscript.py` | Execute script |
| `uv run --with requests myscript.py` | Run with additional packages |

Want to learn about self-contained scripts? See [how to write self-contained Python scripts](https://pydevtools.com/handbook/how-to/how-to-write-a-self-contained-script/).

## Tool Management

| Command | Description |
|---------|-------------|
| `uvx pytest` | Run tool in isolated environment |
| `uv tool install ruff` | Install tool globally |
| `uv tool list` | List installed tools |
| `uv tool upgrade ruff` | Update specific tool |
| `uv tool upgrade --all` | Update all tools |

## Python Version Management

| Command | Description |
|---------|-------------|
| `uv python list` | Show available Python versions |
| `uv python install 3.12` | Install Python version |
| `uv python pin 3.12` | Pin project to version |
| `uv run --python 3.12 python` | Use specific version |

Learn more about [managing Python versions in uv projects](https://pydevtools.com/handbook/how-to/managing-python-versions-in-your-uv-projects/) and [adding Python to your system PATH](https://pydevtools.com/handbook/how-to/how-to-add-python-to-your-system-path-with-uv/).

## Building & Publishing

| Command | Description |
|---------|-------------|
| `uv build` | Build distribution packages |
| `uv publish` | Upload to PyPI |
| `uv publish --publish-url https://test.pypi.org/legacy/` | Upload to TestPyPI |

Ready to publish? Follow our [complete PyPI publishing guide](https://pydevtools.com/handbook/tutorial/publishing-your-first-python-package-to-pypi/).

## Version Management

| Command | Description |
|---------|-------------|
| `uv version` | Show current version |
| `uv version --bump patch` | Increment patch version |
| `uv version --bump minor` | Increment minor version |
| `uv version --bump major` | Increment major version |

## Virtual Environments

| Command | Description |
|---------|-------------|
| `uv venv` | Create virtual environment |
| `uv venv --python 3.12` | Create with specific Python |

New to virtual environments? Read [why you should use a virtual environment](https://pydevtools.com/handbook/explanation/why-should-i-use-a-virtual-environment/).

## Utility Commands

| Command | Description |
|---------|-------------|
| `uv --help` | Show help |
| `uv help sync` | Help for specific command |
| `uv self update` | Update uv itself |
| `uv cache clean` | Clear package cache |

## Common Workflows

### New Project Setup
```bash
uv init myproject
cd myproject
uv add requests pandas
uv add --dev pytest ruff
uv run python main.py
```

### Existing Project
```bash
git clone <repo>
cd <repo>
uv sync
uv run pytest
```

Need help with testing? Check out [setting up testing with pytest and uv](https://pydevtools.com/handbook/tutorial/setting-up-testing-with-pytest-and-uv/) and [how to run tests using uv](https://pydevtools.com/handbook/how-to/how-to-run-tests-using-uv/).

### Quick Script
```bash
uv init --script analyze.py
uv add --script analyze.py pandas matplotlib
uv run analyze.py
```

## Configuration

### pyproject.toml Essentials
```toml
[project]
name = "myproject"
version = "0.1.0"
dependencies = ["requests>=2.28.0"]

[tool.uv]
dev-dependencies = [
    "pytest>=7.0",
    "ruff>=0.1.0",
]
```

### Environment Variables
- `UV_CACHE_DIR` - Set cache directory
- `UV_PYTHON_INSTALL_DIR` - Python installation location
- `UV_INDEX_URL` - Default package index

## Tips

- Most commands accept `--python 3.x` to specify version
- Use `--with package` to add temporary dependencies
- `uv sync --locked` enforces exact lockfile versions
- `uv run` automatically manages virtual environments

</article>
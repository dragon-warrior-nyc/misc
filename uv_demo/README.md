# UV Demo Project

A minimal demonstration of using [uv](https://github.com/astral-sh/uv) for Python project management.

## What is uv?

uv is a fast Python package installer and resolver, designed as a drop-in replacement for pip and pip-tools. It's written in Rust and is significantly faster than traditional tools.

## Prerequisites

Install uv:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on macOS with Homebrew:
```bash
brew install uv
```

Verify the installation:
```bash
uv --version
```

## Creating a New Project from Scratch

To create your own Python project using uv:

### 1. Create Project Directory and Structure

```bash
# Create virtual environment (uv will use Python 3.11 from .python-version)
mkdir my-project && cd my-project

# Create a package directory (matching your project name)
mkdir my_project
touch my_project/__init__.py
touch my_project/main.py
```

### 2. Initialize with uv

```bash
# Create a virtual environment with Python 3.11
uv venv --python 3.11

# Activate it
source .venv/bin/activate  # On macOS/Linux
# or
.venv\Scripts\activate     # On Windows
```

### 3. Create pyproject.toml

Create a `pyproject.toml` file with your project configuration:

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
requires-python = ">=3.11"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

### 4. Add Dependencies

```bash
# Add runtime dependencies (needed to run your application)
uv add requests
uv add pandas numpy

# Add development dependencies (only needed during development)
uv add --dev pytest ruff black
```

**What are development dependencies?**
- **Runtime dependencies** (`uv add`): Required for your application to run (e.g., requests, pandas)
- **Development dependencies** (`uv add --dev`): Only needed during development, testing, or building (e.g., pytest for testing, ruff for linting, black for formatting)

Development dependencies are stored separately in `pyproject.toml` under `[project.optional-dependencies]` or `[dependency-groups]` and won't be installed in production environments.

This automatically updates your `pyproject.toml` file. After adding dependencies, it might look like:

```toml
[project]
name = "my-project"
version = "0.1.0"
dependencies = [
    "requests>=2.31.0",
    "pandas>=2.0.0",
]

[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.1.0",
]
```

**How `uv sync` uses this information:**
- `uv sync` - Installs both runtime AND development dependencies (default)
- `uv sync --no-dev` - Installs only runtime dependencies (for production)
- `uv sync --only-dev` - Installs only development dependencies

This allows you to have different dependency sets for development vs production environments.

### 5. Pin Python Version (Optional)

```bash
echo "3.11" > .python-version
```

### 6. Sync and Install

```bash
uv sync
```

Your project is now ready! Write your code in `my_project/` and run it.

## Using This Demo Project

This project requires Python 3.11 and demonstrates basic uv usage.

### 1. Create a Virtual Environment

```bash
# uv will automatically use Python 3.11 as specified in pyproject.toml
uv venv
```

### 2. Activate the Virtual Environment

```bash
# On macOS/Linux
source .venv/bin/activate

# On Windows
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
# Sync and install all dependencies from pyproject.toml
uv sync
```

### 4. Run the Demo

```bash
python run_demo.py
```

## Key uv Commands

- `uv venv` - Create a virtual environment
- `uv pip install <package>` - Install a package
- `uv pip list` - List installed packages
- `uv pip freeze` - Show installed packages in requirements format
- `uv sync` - Sync dependencies from pyproject.toml
- `uv add <package>` - Add a dependency to pyproject.toml
- `uv remove <package>` - Remove a dependency

## Why use uv?

- ⚡ **Fast**: 10-100x faster than pip
- 🔒 **Reliable**: Built-in dependency resolution
- 🎯 **Simple**: Drop-in replacement for pip
- 📦 **Modern**: Uses pyproject.toml standard

## Project Structure

```
uv_demo/
├── pyproject.toml    # Project configuration and dependencies
├── run_demo.py       # Entry point script
├── uv_demo/          # Package directory
│   ├── __init__.py   # Package initialization
│   └── main.py       # Demo script with external dependency
└── README.md         # This file
```

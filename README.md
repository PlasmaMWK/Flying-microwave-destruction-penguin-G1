# RPG project for Agile course

## Prerequies

Before you begin, make sure you have the following installed on your environment:

- Python (version 3.x recommended)
- Pip (package manager for Python)
- Pipenv (tool for managing virtual environments and dependencies)

### Installing Pipenv

If Pipenv is not already installed, you can install it using pip:

```bash
pip install pipenv
```

### Loading the Project Packages

```bash
pipenv install
```

### Activating the Virtual Environment

```bash
pipenv shell
```

Once activated, you should see the name of the virtual environment in your command prompt.

## To run all tests in the virtual environment :

```python
pipenv run python3 -m unittest discover -s test
```

### Git structure

We will use the following structure for our repository:

- main : this branch is the main branch and reflect the current production version, we should never push directly on main
- dev : this branch is the current development branch where developers will push their commits, via **Pull Requests**. We should never push directly on dev.
- features/\* : Every features should be develop on a specific feature branch.

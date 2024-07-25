# yw_generator

This is a template project for generating YesWorkflow Syntax from Python code.

## Installation

```bash
git clone <url>
cd yw_generator
pip install .
```

### Python

This returns the YesWorkflow syntax commented Python code:

```python
import yw_generator
yw = yw_generator.yw_generator('a = 1')
```

### Command Line

This prints out the YesWorkflow syntax commented Python code:

```bash
ywgenerator example.py
```

---

## Ideas

- Make comments to `@BEGIN` and `@END` blocks
- Have parameter for the depth of the graph, or simply use comments to segment the code. 

## TODO

- [ ] A working prototype.
- [ ] Set up readthedocs
- [ ] GitHub workflow for testing, code formatting and linting. 

## Contributing Guide

### First Step and Start Here

- [ ] Make this work first:
  ```bash
  python yw_generator.py ../../tests/raw.py
  ```

### Using `tox` to Test, Do Code-Formatting, and Linting

> I think we can ignore this testing and formatting section for now. Do this after we have a working prototype.

We use [`tox`](https://tox.wiki/en/4.11.3/installation.html) to run:
  - Python unit test ([`pytest`](https://docs.pytest.org/en/7.4.x/))
  - Converting old string to f-string ([`flynt`](https://github.com/ikamensh/flynt#flynt---string-formatting-converter))
  - Code formatting ([`black`](https://black.readthedocs.io/en/stable/))
  - Sort import order ([`isort`](https://pycqa.github.io/isort/index.html))
  - Linting ([`flake8`](https://flake8.pycqa.org/en/latest/))

#### Python Unit test
```bash
tox
```

#### Converting Old String to F-String
```bash
tox -e fstring
```

#### Code Formatting
```bash
tox -e format
```

#### Sort Import Order
```bash
tox -e sort_import
```

#### Linting
```bash
tox -e lint
```

### Pre-Commit

We use [pre-commit](https://pre-commit.com/#install) to check code format and style before committing:
  - Converting old string to f-string ([`flynt`](https://github.com/ikamensh/flynt#flynt---string-formatting-converter))
  - Code formatting ([`black`](https://black.readthedocs.io/en/stable/))
  - Sort import order ([`isort`](https://pycqa.github.io/isort/index.html))
  - Linting ([`flake8`](https://flake8.pycqa.org/en/latest/))

Set up pre-commit for the first time:
```bash
pre-commit install
```

Check every file:
```bash
pre-commit run --all-files
```


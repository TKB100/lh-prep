# Python Automation Suite

![CI](https://github.com/TKB100/python-automation-suite/actions/workflows/test.yml/badge.svg)

A collection of Python automation tools demonstrating real-world software engineering skills including subprocess automation, CLI tooling, file I/O, object-oriented programming, automated testing with pytest, and CI/CD pipeline configuration with GitHub Actions.

---

## Project Structure

| File | Description |
|------|-------------|
| `automation.py` | Basic subprocess usage — running shell commands from Python and capturing output |
| `check_tool.py` | CLI tool using argparse — checks if a system tool is installed and returns its version |
| `run_checks.py` | Reads a list of tools from `tools.txt` and runs version checks on each one |
| `fundamentals.py` | Core Python fundamentals — list comprehensions, functions, dictionaries |
| `lab_checker.py` | Reads `tools.txt`, checks each tool, and prints a formatted lab environment report |
| `lab_checker_oop.py` | OOP version of lab_checker — uses the `Tool` class for cleaner, modular design |
| `oop.py` | Defines the `Tool` class with methods for checking installation, version parsing, and status reporting |
| `test_tools.py` | pytest test suite — validates `check_tool()` against known installed and missing tools |
| `tools.txt` | Input file — list of tools to check (one per line) |
| `.github/workflows/test.yml` | GitHub Actions CI/CD pipeline — runs pytest on every push |

---

## Skills Demonstrated

- **subprocess** — executing shell commands programmatically and handling output/errors
- **argparse** — building command-line tools with flags and arguments
- **File I/O** — reading and processing text files with proper resource management
- **try/except** — graceful error handling for missing tools and runtime failures
- **OOP** — class design with `__init__`, methods, and encapsulated behavior
- **pytest** — automated test suites with pass/fail assertions
- **CI/CD** — GitHub Actions pipeline that automatically runs tests on every push
- **Debugging** — diagnosed and resolved a pipeline failure caused by top-level module execution on import

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/TKB100/python-automation-suite.git
cd python-automation-suite
pip install pytest
```

### Running the Lab Checker

```bash
python3 lab_checker.py
```

Example output:
```
===== Lab Environment Report =====
✅ git        | version: 2.39.5
✅ python3    | version: 3.13.2
❌ node       | version: unknown
==================================
```

### Checking a Specific Tool

```bash
python3 check_tool.py --tool git
python3 check_tool.py --tool python3
```

### Running Tests

```bash
pytest test_tools.py
```

### Running the OOP Version

```bash
python3 lab_checker_oop.py
```

---

## CI/CD Pipeline

This project uses GitHub Actions to automatically run the test suite on every push.

The pipeline:
1. Spins up a fresh Ubuntu machine
2. Installs Python 3.13
3. Installs pytest
4. Runs `pytest test_tools.py`
5. Reports pass or fail

Pipeline configuration: `.github/workflows/test.yml`

**Pipeline Debugging Story:** During development the pipeline failed with an `IndexError` caused by top-level code in `run_checks.py` executing on import. Fixed by wrapping executable code in an `if __name__ == '__main__'` block — a standard Python pattern that prevents module-level code from running during imports.

---

## Author

**Triston Barrientos**
CS Senior — Texas Tech University (May 2026)
[LinkedIn](https://linkedin.com/in/triston00barrientos) | [GitHub](https://github.com/TKB100)


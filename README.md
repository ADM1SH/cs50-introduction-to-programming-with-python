# CS50P: Introduction to Programming with Python

[![Language: Python](https://img.shields.io/badge/Language-Python_3.10+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Course: CS50P](https://img.shields.io/badge/Course-Harvard_CS50P-red.svg)](https://cs50.harvard.edu/python/)
[![Code Style: Black](https://img.shields.io/badge/Code%20Style-Black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Solutions, problem sets, and practical exercises for Harvard University's CS50P: CS50's Introduction to Programming with Python.

## Description
This repository contains code written for CS50P, teaching programming through Python. The course emphasizes writing clean, readable, and robust code using standard language paradigms, standard library modules, unit testing, and object-oriented principles.

### Key Concepts Practiced
* **Functions & Variables**: Function definitions, parameters, return values, type conversions, scope, and mathematical expressions (`calculator.py`, `calculator2.py`).
* **Conditionals & Loops**: Control flow statements, boolean logic, `match-case`, `while` and `for` iteration patterns.
* **Exceptions**: Input validation, error catching with `try-except-else-finally`, and raising intentional exceptions.
* **Libraries & Packages**: Leveraging Python standard library modules (`math`, `random`, `sys`) and PyPI third-party tools.
* **Unit Testing**: Writing deterministic test suites using `pytest` to verify function correctness.
* **File I/O & Regular Expressions**: Reading and writing CSV/text files, clean string parsing, and regex pattern matching (`re` module).
* **Object-Oriented Programming**: Defining classes, methods, instance variables, properties, decorators (`@property`), and operator overloading.

## Repository Contents
```text
CS50 Introduction to programming with python/
├── hello.py            # Basic input/output formatting and string methods
├── hello2.py           # Structured greeting function with default arguments
├── calculator.py       # Floating-point arithmetic, rounding, and formatting
├── calculator2.py      # Modular arithmetic functions with defensive assertions
└── README.md           # Coursework documentation
```

## Requirements
* Python: version 3.10 or higher
* Package manager: `pip`
* Test framework: `pytest`

## Installation
Clone the repository:
```bash
git clone https://github.com/ADM1SH/cs50-introduction-to-programming-with-python.git
cd "cs50-introduction-to-programming-with-python"
```

Install test dependencies:
```bash
pip install pytest black flake8
```

## Usage
Run any Python script directly:
```bash
python3 calculator.py
```

Format code according to PEP 8 standards:
```bash
black .
```

## Support
Submit issues or questions to the repository tracker:
https://github.com/ADM1SH/cs50-introduction-to-programming-with-python/issues

## Roadmap
* [x] Complete Week 0 (Functions, Variables).
* [x] Complete Week 1 (Conditionals).
* [x] Complete Week 2 (Loops).
* [x] Complete Week 3 (Exceptions).
* [x] Complete Week 4 (Libraries).
* [x] Complete Week 5 (Unit Tests).
* [x] Complete Week 6 through Week 8 (File I/O, Regular Expressions, OOP).

## Contributing
1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/new-solution`.
3. Verify formatting with `flake8` and `black`.
4. Commit your changes: `git commit -m "feat: add problem set solution"`.
5. Open a Pull Request.

## Authors and Acknowledgment
* **Adam Anwar** (ADM1SH) - Problem set solutions.
* **David J. Malan and CS50 Staff** - Harvard University instructional design.

## License
MIT License. See `LICENSE` for details.

## Project Status
Completed coursework repository. Serves as a reference for foundational Python programming.

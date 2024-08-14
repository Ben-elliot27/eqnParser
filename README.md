# Calculator GUI with Parser-Based Equation Evaluation

## Overview

This project is a Python-based calculator with a graphical user interface (GUI) built using PyQt5. The main goal of this project is not just to create a functional calculator, but to explore and learn about parsing techniques using programming languages. The calculator evaluates mathematical expressions input by the user as strings, which are parsed and processed by a custom parser implemented in Python. This project was worked on jointly with @JamesMartinGithub.

## Features

- **GUI Interface**: The application features a clean and simple GUI, which allows users to input mathematical expressions and see results.
- **Custom Parser**: The core of this project is the custom parser that interprets mathematical expressions, following the order of operations (BIDMAS/BODMAS).
- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, division, modulo, exponentiation, and floor division.
- **Bracket Handling**: The parser correctly handles operations inside brackets, allowing for complex expressions.
- **Error Handling**: Basic error handling for common syntax errors like unmatched brackets and unsupported characters.
- **Extendable Design**: The project is designed with extensibility in mind, with TODOs and placeholders for future enhancements like trigonometric functions, square root operations, and algebraic support.

## **Run the application**:
   ```bash
   python GUI.py
   ```

## Files and Structure

- **`GUI.py`**: This is the main script that launches the calculator application. It sets up the GUI using PyQt5 and integrates the parser from `Interpreter.py` for evaluating expressions.
- **`Interpreter.py`**: This file contains the core logic for parsing and evaluating mathematical expressions. It includes a lexer that tokenizes the input string, a parser that processes these tokens according to BIDMAS, and evaluation functions.

## How It Works

### Parsing and Evaluation Process

1. **Lexing**: The input string is split into tokens, distinguishing numbers from operators.
2. **Brackets Handling**: If brackets are present, the parser first processes the innermost brackets and evaluates the expressions within.
3. **BIDMAS Parsing**: The parser evaluates the expression based on BIDMAS (Brackets, Indices, Division and Multiplication, Addition, and Subtraction).
4. **Evaluation**: The evaluated result is then returned and displayed on the GUI.

### GUI Functionality

- **Expression Input**: Users can input expressions via buttons or directly into a text box.
- **Real-Time Calculation**: As expressions are entered, the user can press the "=" button to calculate and display the result.
- **Basic Functionality**: Includes buttons for numbers, basic operators, and some advanced operations like square and square root.

## TODOs and Future Enhancements

- **Improve GUI**: Enhance the look and feel of the buttons and interface.
- **Advanced Mathematical Functions**: Add support for trigonometric functions, logarithms, and more.
- **Enhanced Error Handling**: Improve error detection and user feedback for invalid inputs.
- **Performance Optimization**: Compare and optimize the custom parser against Python's built-in `eval()` function.
- **Algebraic Expression Support**: Extend the parser to handle algebraic expressions and variables.

## Contributing

Contributions to improve the calculator, the parser, or the GUI are welcome. Please fork the repository, make your changes, and submit a pull request.

## Credit

This project was worked on jointly with @JamesMartinGithub 

---

Feel free to modify and extend this project to suit your learning or application needs!

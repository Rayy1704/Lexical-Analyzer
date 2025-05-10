# Tokenization of C++ Code: A Python Approach Using Regular Expressions


## Overview

PyLexer is a lightweight lexical analyser manually implemented in Python using the built-in `re` module. It is designed to tokenize a simplified subset of the C++ programming language. The project demonstrates core compiler design concepts such as tokenization, regular expressions, and pattern prioritization — providing hands-on insight into the inner workings of a compiler front-end.

This tool is ideal for educational purposes, particularly in understanding how lexical analysis transforms source code into a stream of tokens for further processing.

## Tools

![vscode](https://skillicons.dev/icons?i=vscode) ![github](https://skillicons.dev/icons?i=github) ![git](https://skillicons.dev/icons?i=git) 

## Languages & Frameworks

![python](https://skillicons.dev/icons?i=python) ![cpp](https://skillicons.dev/icons?i=cpp) ![regex](https://skillicons.dev/icons?i=regex)

## Resources

![stackoverflow](https://skillicons.dev/icons?i=stackoverflow)

## Installation & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/Rayy1704/Lexical-Analyzer/
cd Lexical-Analyzer
```

### 2. Run the Lexer

```bash
python lexer.py <input_file.cpp> <output_file.txt>
```

> Example:
```bash
python lexer.py sample.cpp tokens.txt
```

## Token Types

| Token Type     | Description                                       |
|----------------|---------------------------------------------------|
| Header         | C++ include directives                            |
| Keyword        | Reserved C++ words (e.g., int, return)            |
| Identifier     | Variable, function names, etc.                    |
| Operator       | Arithmetic/logical symbols (+, ==, <=, etc.)      |
| Literal        | Numbers (10, 3.14) and strings ("Hello")          |
| Separator      | Braces, semicolons, commas, etc.                  |
| Comment        | Single-line // comments                           |
| Whitespace     | Ignored                                           |

## Example

### Sample Input (input.cpp)

```cpp
#include <string>
string name = "Rayyan"; // store my name in variable
```

### Output

```
Line 1: Token = #include <string> → Header
Line 2: Token = string           → Keyword
Line 2: Token = name             → Identifier
Line 2: Token = =                → Operator
Line 2: Token = "Rayyan"         → String Literal
Line 2: Token = //...            → Comment
```

## Testing & Evaluation

- Compared with Flex using identical test cases.
- Functional testing on C++ programs with declarations, control structures, expressions, comments.

## Challenges Faced

| Challenge                          | Solution                                      |
|-----------------------------------|-----------------------------------------------|
| Identifier vs. keyword ambiguity  | Post-check keyword list after identifier match |
| Nested symbols and punctuation    | Regex priority and multi-char pattern matching |
| CLI input handling                | Used sys.argv with validation and error output |
| Missing input files               | try-except block for FileNotFoundError         |

## Lessons Learned

- Regex pattern order affects correctness and precision.
- Manual lexical analysis reinforces compiler theory.
- Python's `re` module supports complex token extraction.
- Importance of meaningful errors and clean CLI usage.

## Future Extensions

- Extend grammar for broader C++ syntax coverage
- Integrate a parser for further compilation stages

## Acknowledgments

- Prof. Charles Severance – Python for Everybody, Coursera

import re
import sys

# C++ reserved keywords
KEYWORDS = {
    'int', 'float', 'bool', 'string', 'if', 'else', 'while',
    'for', 'return', 'void', 'char', 'double', 'true', 'false',
    'alignas', 'alignof', 'and', 'and_eq', 'asm', 'auto', 'bitand',
    'bitor', 'break', 'case', 'catch', 'char16_t', 'char32_t', 'class',
    'compl', 'concept', 'const', 'consteval', 'constexpr', 'constinit',
    'continue', 'co_await', 'co_return', 'co_yield', 'decltype', 'default',
    'delete', 'do', 'dynamic_cast', 'else', 'enum', 'explicit', 'export',
    'extern', 'false', 'final', 'float', 'for', 'friend', 'goto', 'if',
    'inline', 'int', 'long', 'mutable', 'namespace', 'new', 'noexcept', 'not',
    'not_eq', 'nullptr', 'operator', 'or', 'or_eq', 'private', 'protected',
    'public', 'reflexpr', 'register', 'reinterpret_cast', 'requires', 'return',
    'short', 'signed', 'sizeof', 'static', 'static_assert', 'static_cast', 'struct',
    'switch', 'template', 'this', 'thread_local', 'throw', 'true', 'try', 'typedef',
    'typeid', 'typename', 'union', 'unsigned', 'using', 'virtual', 'void', 'volatile',
    'wchar_t', 'while', 'xor', 'xor_eq'
}


# Token regular expression patterns
token_specification = [
    ('HEADER',           r'#include\s*<[^>]+>|#include\s*"[^"]+"'),       # Header Files
    ('PREPROCESSOR_DIRECTIVES', r'#\s*(define|ifdef|ifndef|endif|undef|pragma)\b[^\n]*'), # Pre-processor directives
    ('COMMENT',          r'//[^\n]*'),                 # Single-line comment
    ('MULTILINE_COMMENT',r'/\*[\s\S]*?\*/'),           # Multi-line comment
    ('FLOAT_LITERAL',    r'\b\d+\.\d+\b'),             # Float
    ('INTEGER_LITERAL',  r'\b\d+\b'),                  # Integer
    ('STRING_LITERAL',   r'"[^"\n]*"'),                # String
    ('OPERATOR',         r'<<|>>|==|!=|<=|>=|\+\+|--|[-+*/=<>]'),  # Operators
    ('SEPARATOR',        r'[(){}\[\];,]'),             # Separators
    ('IDENTIFIER',       r'\b[A-Za-z_][A-Za-z0-9_]*\b'),# Identifiers
    ('WHITESPACE',       r'[ \t\r]+'),                 # Spaces/tabs
    ('NEWLINE',          r'\n'),                       # Newlines
    ('UNKNOWN',          r'.'),                        # Anything not mentioned above
]

# Compile into one regular expression
# The regular expression greedy algorithem will match the longest possible token first
tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)

# Determine final token type label
def classify_token(name, value):
    if name == 'IDENTIFIER':
        return 'Keyword' if value in KEYWORDS else 'Identifier'
    elif name == 'FLOAT_LITERAL':
        return 'Float Literal'
    elif name == 'INTEGER_LITERAL':
        return 'Integer Literal'
    elif name == 'STRING_LITERAL':
        return 'String Literal'
    elif name == 'OPERATOR':
        return 'Operator'
    elif name == 'SEPARATOR':
        return 'Separator'
    elif name == 'COMMENT':
        return 'Comment'
    elif name == 'MULTILINE_COMMENT':
        return 'Multi-Line Comment'
    elif name == 'HEADER':
        return 'Header'
    elif name == 'UNKNOWN':
        return 'Unknown'
    elif name == 'PREPROCESSOR_DIRECTIVES':
        return 'Preprocessor Directive'
    else:
        return None

# Analyze the input file and write tokens to output file
def analyze_file(input_path, output_path='output.txt'):
    # error handling - 1 : Check if input file has .cpp extension
    if not input_path.endswith('.cpp'):
        print(f"Error: The file '{input_path}' must be a C++ file with .cpp extension.")
        sys.exit(1)
        
    # error handling - 2 : Check if output file has .txt extension
    if not output_path.endswith('.txt'):
        print(f"Error: The output file '{output_path}' must have a .txt extension.")
        sys.exit(1)
        
    try:
        # Try to open and read the input file
        with open(input_path, 'r', encoding='utf-8') as file:
            code = file.read()
            
            # error handling - 3 : Check if file is empty
            if not code.strip():
                print(f"Error: The file '{input_path}' is empty.")
                sys.exit(1)

        line_num = 1
        results = []

        for match in re.finditer(tok_regex, code):
            kind = match.lastgroup
            value = match.group()

            if kind == 'NEWLINE':
                line_num += 1
                continue
            if kind == 'WHITESPACE':
                continue

            token_type = classify_token(kind, value)
            if token_type:
                results.append(f"Line {line_num}: Token = {value:<12} → {token_type}")

        # Try to write to output file
        try:
            with open(output_path, 'w', encoding='utf-8') as out_file:
                for line in results:
                    out_file.write(line + '\n')
        except PermissionError:
            # error handling - 4 : Check if output file is writable
            print(f"Error: Cannot write to '{output_path}'. Permission denied.")
            sys.exit(1)
        except IOError as e:
            # error handling - 5 : Handle other I/O errors during writing
            print(f"Error: Failed to write to output file '{output_path}': {str(e)}")
            sys.exit(1)

        print(f"Token analysis written to: {output_path}")
    except FileNotFoundError:
        # error handling - 6 : Check if input file exists
        print(f"Error: Could not open file '{input_path}'. The file does not exist .")
        sys.exit(1)
    except PermissionError:
        # error handling - 7 : Check if input file is readable
        print(f"Error: Cannot read from '{input_path}'. Permission denied.")
        sys.exit(1)
    except UnicodeDecodeError:
        # error handling - 8 : Check for invalid characters in input file
        print(f"Error: The file '{input_path}' contains invalid characters. Please ensure it is a valid UTF-8 encoded file.")
        sys.exit(1)
    except Exception as e:
        # error handling - 9 : Handle unexpected errors
        print(f"Error: An unexpected error occurred: {str(e)}")
        sys.exit(1)

# CLI entry point
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lexer.py <input_file> [output_file]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'output.txt'
    analyze_file(input_file, output_file)

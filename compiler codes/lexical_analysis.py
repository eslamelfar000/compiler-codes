# Define the token types
INT = 'INT'
PLUS = 'PLUS'
EQ = 'EQ'
MINUS = 'MINUS'
MULT = 'MULT'
DIV = 'DIV'
LPAREN = 'LPAREN'
RPAREN = 'RPAREN'
IDF = 'IDF'
EOF = 'EOF'

# Define a dictionary of keywords
KEYWORDS = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'print': 'PRINT',
}


# Define a function to tokenize the input string
def tokenize(input_string):
    tokens = []
    pos = 0
    while pos < len(input_string):
        current_char = input_string[pos]

        # Integer token
        if current_char.isdigit():
            value = ''
            while pos < len(input_string) and input_string[pos].isdigit():
                value += input_string[pos]
                pos += 1
            tokens.append(('INT', int(value)))

        # Identifier or keyword token
        elif current_char.isalpha() or current_char == '_':
            value = ''
            while pos < len(input_string) and (input_string[pos].isalnum() or input_string[pos] == '_'):
                value += input_string[pos]
                pos += 1
            token_type = KEYWORDS.get(value, IDF)
            tokens.append((token_type, value))

        # Operator tokens
        elif current_char == '+':
            tokens.append((PLUS, current_char))
            pos += 1
        elif current_char == '-':
            tokens.append((MINUS, current_char))
            pos += 1
        elif current_char == '*':
            tokens.append((MULT, current_char))
            pos += 1
        elif current_char == '/':
            tokens.append((DIV, current_char))
            pos += 1
        elif current_char == '(':
            tokens.append((LPAREN, current_char))
            pos += 1
        elif current_char == ')':
            tokens.append((RPAREN, current_char))
            pos += 1
        elif current_char == '=':
            tokens.append((EQ, current_char))
            pos += 1

        # Ignore whitespace
        elif current_char.isspace():
            pos += 1

        # Invalid input
        else:
            print(f"Invalid input: {current_char}")
            return []

    tokens.append((EOF, None))
    return tokens


# Test the tokenizer
data = '''
sum = 2 + 3 - 5
result = sum * 4
if( x = 9)
'''
tokens = tokenize(data)
print(tokens)

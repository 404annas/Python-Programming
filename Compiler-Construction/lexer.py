def lexical_analyzer_extended(source_code):
    tokens = []
    errors = []
    i = 0
    line = 1

    KEYWORDS = {'if', 'else', 'while'}
    OPERATORS = {'+', '-', '*', '/', '=', '==', '<', '>'}
    PUNCTUATION = {'(', ')', '{', '}', ';'}

    while i < len(source_code):
        char = source_code[i]

        # 1. Whitespace
        if char.isspace():
            if char == '\n':
                line += 1
            i += 1
            continue

        # 2. Single-line comment
        if char == '/' and i + 1 < len(source_code) and source_code[i+1] == '/':
            while i < len(source_code) and source_code[i] != '\n':
                i += 1
            continue

        # 3. Multi-line comment /* ... */
        if char == '/' and i + 1 < len(source_code) and source_code[i+1] == '*':
            i += 2
            while i + 1 < len(source_code) and not (source_code[i] == '*' and source_code[i+1] == '/'):
                if source_code[i] == '\n':
                    line += 1
                i += 1
            i += 2  # Skip */
            continue

        # 4. String literals "..."
        if char == '"':
            lexeme = ''
            i += 1
            while i < len(source_code) and source_code[i] != '"':
                if source_code[i] == '\n':
                    errors.append(f"Unclosed string literal at line {line}")
                    break
                lexeme += source_code[i]
                i += 1
            else:
                i += 1  # Skip closing "
            tokens.append(('STRING', lexeme))
            continue

        # 5. Identifiers / Keywords
        if char.isalpha():
            lexeme = ''
            while i < len(source_code) and source_code[i].isalnum():
                lexeme += source_code[i]
                i += 1
            token_type = 'KEYWORD' if lexeme in KEYWORDS else 'IDENTIFIER'
            tokens.append((token_type, lexeme))
            continue

        # 6. Numbers
        if char.isdigit():
            lexeme = ''
            while i < len(source_code) and source_code[i].isdigit():
                lexeme += source_code[i]
                i += 1
            tokens.append(('NUMBER', lexeme))
            continue

        # 7. Operators
        if char in OPERATORS or (char == '=' and i + 1 < len(source_code) and source_code[i+1] == '='):
            if char == '=' and i + 1 < len(source_code) and source_code[i+1] == '=':
                tokens.append(('OPERATOR', '=='))
                i += 2
            else:
                tokens.append(('OPERATOR', char))
                i += 1
            continue

        # 8. Punctuation
        if char in PUNCTUATION:
            tokens.append(('PUNCTUATION', char))
            i += 1
            continue

        # 9. Errors
        errors.append(f"Invalid character '{char}' at line {line}")
        i += 1

    # Token count by type
    token_count = {}
    for t_type, _ in tokens:
        token_count[t_type] = token_count.get(t_type, 0) + 1

    return tokens, errors, token_count

# -------------------------
# Sample Input Program
source_code = '''
x = "hello";
y = 5; /* multi-line
comment */
while (x < y) {
    x = x + 1;
    z = x @ 3; // invalid char
}
'''

# Run the lexer
tokens, errors, token_count = lexical_analyzer_extended(source_code)

# Print results
print("Tokens:")
for t in tokens:
    print(t)

print("\nErrors:")
for e in errors:
    print(e)

print("\nToken Count:")
for k,v in token_count.items():
    print(f"{k}: {v}")

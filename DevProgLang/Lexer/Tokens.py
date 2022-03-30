# package DevProgLang/Lexer/Tokens.py
INT = 'INT'
FLOAT = 'FLOAT'
ID = 'ID_VAR'
OP = '_OP'
KW = 'KW_'
RESERVED = 'RESERVED'

# Token's List
token_exprs = [
    (r'[\n]+', 'NEWLINE'),
    (r'[ \t]+', None),
    (r'#.*|//.*', 'COMMENT'),
    (r'[/]\*([^#]*)\*[/]', 'MULTILINE_COMMENT'),
    (r'[+-]*[0-9]+\.[0-9]+', FLOAT),
    (r'[+-]*[1-9]+|0', INT),
    (r'\'', 'MARKS'),
    (r'\"', 'DOUBLE_QUOTES'),
    (r'\(', 'L_BRACKET'),
    (r'\)', 'R_BRACKET'),
    (r'\{', 'L_BRACE'),
    (r'\}', 'R_BRACE'),
    (r'\[', 'L_SQUARE_BRACKET'),
    (r'\]', 'R_SQUARE_BRACKET'),
    (r'\+', 'PLUS' + OP),
    (r'-', 'MINUS' + OP),
    (r'\.', 'POINT'),
    (r'\,', 'COMMA'),
    (r'\*', 'MULTIPLICATION' + OP),
    (r'/', 'SLASH'),
    (r'<=', 'LESS_EQUALLY' + OP),
    (r'<', 'LESS' + OP),
    (r'>=', 'MORE' + OP),
    (r'>', 'MORE' + OP),
    (r':=|=', 'ASSIGN' + OP),
    (r'!=', 'NOT_EQUALLY' + OP),
    (r'\:', 'COLON'),
    (r'\;', 'SEMICOLON'),
    (r'true', KW + 'TRUE'),
    (r'false', KW + 'FALSE'),
    (r'int', KW + 'INT'),
    (r'str', KW + 'STR'),
    (r'float', KW + 'FLOAT'),
    (r'bool', KW + 'BOOL'),
    (r'and', KW + 'AND'),
    (r'or', KW + 'OR'),
    (r'not', KW + 'NOT'),
    (r'if', KW + 'IF'),
    (r'then', KW + 'THEN'),
    (r'else', KW + 'ELSE'),
    (r'while', KW + 'WHILE'),
    (r'do', KW + 'DO'),
    (r'begin', KW + 'begin'),
    (r'end', KW + 'END'),
    (r'input|<<<', KW + 'INPUT'),
    (r'print|>>>', KW + 'PRINT'),
    (r'[A-Za-z][A-Za-z0-9_]*', ID),
]

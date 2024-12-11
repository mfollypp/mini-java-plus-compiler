import re


# region Token
class Token:
    def __init__(self, kind, value, line, column):
        self.kind = kind
        self.value = value
        self.line = line
        self.column = column
# endregion Token


# region Scanner
class Scanner:
    def __init__(self):
        # Regular expressions for different token types
        self.token_specification = [
            ('WHITESPACE',     r'[\n\t\r\f\s]+'),
            ('COMMENT',        r'//.*?$|/\*.*?\*/'), 
            ('RESERVED',       r'\b(?:boolean|class|extends|public|static|void|main|String|return|int|if|else|while|System\.out\.println|length|true|false|this|new|null)\b'),
            ('IDENTIFIER',     r'[a-zA-Z][a-zA-Z0-9_]*'),
            ('NUMBER',         r'\b\d+\b'), 
            ('OPERATOR',       r'[=<>!]=|[+\-*&]|&&|!|\.|;|,|\(|\)|\[|\]|\{|\}'), 
        ]

        self.regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specification), re.DOTALL | re.MULTILINE) # Usa grupo de captura -> funciona da esquerda para direita
        
    def scan(self, code):
        tokens = []
        line = 1
        line_start = 0

        for match in self.regex.finditer(code):
            kind = match.lastgroup # Grupo foi informado no grupo de captura
            value = match.group(kind)
            column = match.start() - line_start
            
            if kind == 'WHITESPACE':
                if '\n' in value:
                    line += value.count('\n')
                    line_start = match.end()
                continue

            elif kind == 'COMMENT':
                if '\n' in value:
                    line += value.count('\n')
                    line_start = match.end()
                continue

            elif kind == 'NUMBER':
                value = int(value)  # Convert number to an integer

            token = Token(kind, value, line, column)
            tokens.append(token)

        return tokens
# endregion Scanner


# region Parser
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        self.current_token = tokens[0] if tokens else None

    def match(self, expected_kind):
        if self.current_token:
            print(f"Matching {expected_kind} with {self.current_token.kind}: {self.current_token.value}")
        if self.current_token and self.current_token.kind == expected_kind:
            self.current_index += 1
            self.current_token = (
                self.tokens[self.current_index] if self.current_index < len(self.tokens) else None
            )
        else:
            raise SyntaxError(f"Expected {expected_kind}, found {self.current_token.kind if self.current_token else 'EOF'}")


    def parse(self):
        # Start parsing from the starting rule of the grammar
        return self.parse_PROG()

    # Recursive functions for non-terminals
    def parse_PROG(self):
        self.parse_MAIN()
        while self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'class':
            self.parse_CLASSE()

    def parse_MAIN(self):
        self.match('RESERVED')  # class
        self.match('IDENTIFIER')  # id
        self.match('OPERATOR')  # '{'
        self.match('RESERVED')  # public
        self.match('RESERVED')  # static
        self.match('RESERVED')  # void
        self.match('RESERVED')  # main
        self.match('OPERATOR')  # '('
        self.match('RESERVED')  # String
        self.match('OPERATOR')  # '['
        self.match('OPERATOR')  # ']'
        self.match('IDENTIFIER')  # id
        self.match('OPERATOR')  # ')'
        self.match('OPERATOR')  # '{'
        self.parse_CMD_LIST()
        self.match('OPERATOR')  # '}'
        self.match('OPERATOR')  # '}'

    def parse_CLASSE(self):
        self.match('RESERVED')  # class
        self.match('IDENTIFIER')  # id
        if self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'extends':
            self.match('RESERVED')  # extends
            self.match('IDENTIFIER')  # id
        self.match('OPERATOR')  # '{'
        self.parse_VAR_LIST()
        self.parse_METODO_LIST()
        self.match('OPERATOR')  # '}'

    def parse_VAR_LIST(self):
        while self.current_token and self.current_token.kind in ('RESERVED', 'IDENTIFIER'):
            self.parse_VAR()

    def parse_VAR(self):
        self.parse_TIPO()
        self.match('IDENTIFIER')
        self.match('OPERATOR')  # ';'

    def parse_METODO_LIST(self):
        while self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'public':
            self.parse_METODO()

    def parse_METODO(self):
        self.match('RESERVED')  # public
        self.parse_TIPO()
        self.match('IDENTIFIER')
        self.match('OPERATOR')  # '('
        if self.current_token and self.current_token.kind in ('RESERVED', 'IDENTIFIER'):
            self.parse_PARAMS()
        self.match('OPERATOR')  # ')'
        self.match('OPERATOR')  # '{'
        self.parse_VAR_LIST()
        self.parse_CMD_LIST()
        self.match('RESERVED')  # return
        self.parse_EXP()
        self.match('OPERATOR')  # ';'
        self.match('OPERATOR')  # '}'

    def parse_TIPO(self):
        if self.current_token.kind == 'RESERVED':
            if self.current_token.value in ('int', 'boolean'):
                self.match('RESERVED')
                if self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '[':
                    self.match('OPERATOR')  # '['
                    self.match('OPERATOR')  # ']'
            else:
                raise SyntaxError(f"Invalid type {self.current_token.value}")
        elif self.current_token.kind == 'IDENTIFIER':
            self.match('IDENTIFIER')
        else:
            raise SyntaxError(f"Invalid type {self.current_token.kind}")

    def parse_CMD_LIST(self):
        while self.current_token and self.current_token.kind != 'OPERATOR' or self.current_token.value != '}':
            self.parse_CMD()

    def parse_CMD(self):
        if self.current_token.kind == 'OPERATOR' and self.current_token.value == '{':
            self.match('OPERATOR')  # '{'
            self.parse_CMD_LIST()
            self.match('OPERATOR')  # '}'
        elif self.current_token.kind == 'RESERVED' and self.current_token.value == 'if':
            self.match('RESERVED')  # if
            self.match('OPERATOR')  # '('
            self.parse_EXP()
            self.match('OPERATOR')  # ')'
            self.parse_CMD()
            if self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'else':
                self.match('RESERVED')  # else
                self.parse_CMD()
        elif self.current_token.kind == 'RESERVED' and self.current_token.value == 'while':
            self.match('RESERVED')  # while
            self.match('OPERATOR')  # '('
            self.parse_EXP()
            self.match('OPERATOR')  # ')'
            self.parse_CMD()
        elif self.current_token.kind == 'RESERVED' and self.current_token.value == 'System.out.println':
            self.match('RESERVED')  # System.out.println
            self.match('OPERATOR')  # '('
            self.parse_EXP()
            self.match('OPERATOR')  # ')'
            self.match('OPERATOR')  # ';'
        elif self.current_token.kind == 'IDENTIFIER':
            self.match('IDENTIFIER')
            if self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '=':
                self.match('OPERATOR')  # '='
                self.parse_EXP()
                self.match('OPERATOR')  # ';'
            elif self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '[':
                self.match('OPERATOR')  # '['
                self.parse_EXP()
                self.match('OPERATOR')  # ']'
                self.match('OPERATOR')  # '='
                self.parse_EXP()
                self.match('OPERATOR')  # ';'
            else:
                raise SyntaxError(f"Unexpected token {self.current_token.kind}")
        else:
            raise SyntaxError(f"Invalid command {self.current_token.kind}")
        
    def parse_EXP(self):
        self.parse_REXP()
        while self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '&&':
            self.match('OPERATOR')  # &&
            self.parse_REXP()

    def parse_REXP(self):
        self.parse_AEXP()
        if self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value in ('<', '==', '!='):
            self.match('OPERATOR')  # <, ==, or !=
            self.parse_AEXP()

    def parse_AEXP(self):
        self.parse_MEXP()
        while self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value in ('+', '-'):
            self.match('OPERATOR')  # + or -
            self.parse_MEXP()

    def parse_MEXP(self):
        self.parse_SEXP()
        while self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '*':
            self.match('OPERATOR')  # *
            self.parse_SEXP()

    def parse_SEXP(self):
        if self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value in ('!', '-'):
            self.match('OPERATOR')  # ! or -
            self.parse_SEXP()
        elif self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value in ('true', 'false', 'null'):
            self.match('RESERVED')  # true, false, or null
        elif self.current_token and self.current_token.kind == 'NUMBER':
            self.match('NUMBER')
        elif self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'new':
            self.match('RESERVED')  # new
            if self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'int':
                self.match('RESERVED')  # int
                self.match('OPERATOR')  # [
                self.parse_EXP()
                self.match('OPERATOR')  # ]
            elif self.current_token and self.current_token.kind == 'IDENTIFIER':
                self.match('IDENTIFIER')
                self.match('OPERATOR')  # (
                self.match('OPERATOR')  # )
        elif self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '(':
            self.match('OPERATOR')  # (
            self.parse_EXP()
            self.match('OPERATOR')  # )
        elif self.current_token and self.current_token.kind == 'IDENTIFIER':
            self.match('IDENTIFIER')
            self.parse_PEXP_TAIL()
        elif self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'this':
            self.match('RESERVED')  # this
        else:
            raise SyntaxError(f"Unexpected token {self.current_token.kind}")

    def parse_PEXP_TAIL(self):
        while self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value in ('.', '['):
            if self.current_token.value == '.':
                self.match('OPERATOR')  # .
                self.match('IDENTIFIER')  # Handle dot-access like `.ComputeFac`
                if self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '(':
                    self.match('OPERATOR')  # (
                    if self.current_token and self.current_token.kind not in ('OPERATOR', 'RESERVED', 'NUMBER'):
                        self.parse_EXPS()  # Handle arguments
                    self.match('OPERATOR')  # )
            elif self.current_token.value == '[':
                self.match('OPERATOR')  # [
                self.parse_EXP()
                self.match('OPERATOR')  # ]

    def parse_EXPS(self):
        self.parse_EXP()
        while self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == ',':
            self.match('OPERATOR')  # ,
            self.parse_EXP()

    def parse_CMD_LIST(self):
        while self.current_token and self.current_token.kind != 'OPERATOR' or self.current_token.value != '}':
            self.parse_CMD()

    def parse_CMD(self):
        if self.current_token.kind == 'OPERATOR' and self.current_token.value == '{':
            self.match('OPERATOR')  # {
            self.parse_CMD_LIST()
            self.match('OPERATOR')  # }
        elif self.current_token.kind == 'RESERVED' and self.current_token.value == 'if':
            self.match('RESERVED')  # if
            self.match('OPERATOR')  # (
            self.parse_EXP()
            self.match('OPERATOR')  # )
            self.parse_CMD()
            if self.current_token and self.current_token.kind == 'RESERVED' and self.current_token.value == 'else':
                self.match('RESERVED')  # else
                self.parse_CMD()
        elif self.current_token.kind == 'RESERVED' and self.current_token.value == 'while':
            self.match('RESERVED')  # while
            self.match('OPERATOR')  # (
            self.parse_EXP()
            self.match('OPERATOR')  # )
            self.parse_CMD()
        elif self.current_token.kind == 'RESERVED' and self.current_token.value == 'System.out.println':
            self.match('RESERVED')  # System.out.println
            self.match('OPERATOR')  # (
            self.parse_EXP()
            self.match('OPERATOR')  # )
            self.match('OPERATOR')  # ;
        elif self.current_token.kind == 'IDENTIFIER':
            self.match('IDENTIFIER')
            if self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '=':
                self.match('OPERATOR')  # =
                self.parse_EXP()
                self.match('OPERATOR')  # ;
            elif self.current_token and self.current_token.kind == 'OPERATOR' and self.current_token.value == '[':
                self.match('OPERATOR')  # [
                self.parse_EXP()
                self.match('OPERATOR')  # ]
                self.match('OPERATOR')  # =
                self.parse_EXP()
                self.match('OPERATOR')  # ;
            else:
                # Fallback for unexpected identifiers
                raise SyntaxError(f"Unexpected identifier usage: {self.current_token.value}")
        else:
            raise SyntaxError(f"Invalid command {self.current_token.kind}")


    # Define similar methods for EXP, REXP, AEXP, etc., based on the grammar.
# endregion Parser

# Example usage
if __name__ == "__main__":

    code = """
class Factorial{
    public static void main(String[] a){
        System.out.println(new Fac().ComputeFac(10));
    }
}
    """

    print(f"\nScanning code:\n{code}\n")

    scanner = Scanner()
    tokens = scanner.scan(code)

    for token in tokens:
        print(f"{token.kind}: {token.value} at line {token.line}, column {token.column}")
    print("\n")

    parser = Parser(tokens)
    try:
        parser.parse()
        print("Parsing successful!")
    except SyntaxError as e:
        print(f"Syntax error: {e}")
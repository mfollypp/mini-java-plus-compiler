class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_index = 0
        self.current_token = tokens[0] if tokens else None

    def match(self, expected_kind):
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

    # Define similar methods for EXP, REXP, AEXP, etc., based on the grammar.

# Example Usage
if __name__ == "__main__":
    code = """
    class Factorial {
        public static void main(String[] a) {
            System.out.println(10);
        }
    }
    """
    scanner = Scanner()
    tokens = scanner.scan(code)
    parser = Parser(tokens)
    try:
        parser.parse()
        print("Parsing successful!")
    except SyntaxError as e:
        print(f"Syntax error: {e}")

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
class ParserError(Exception):
    pass

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.grammar = {
            "PROG": [
                ["MAIN", "CLASSE_LIST"]
            ],
            "CLASSE_LIST": [
                ["CLASSE", "CLASSE_LIST"], 
                ["ε"]
            ],
            "MAIN": [
                ["class", "IDENTIFIER", "{", "public", "static", "void", "main", "(", "String", "[", "]", "IDENTIFIER", ")", "{", "CMD_LIST", "}", "}"]
            ],
            "CLASSE": [
                ["class", "IDENTIFIER", "CLASSE_EXT", "{", "VAR_LIST", "METODO_LIST", "}"]
            ],
            "CLASSE_EXT": [
                ["extends", "IDENTIFIER"], 
                ["ε"]
            ],
            "VAR_LIST": [
                ["VAR", "VAR_LIST"],
                ["ε"]
            ],
            "METODO_LIST": [
                ["METODO", "METODO_LIST"], 
                ["ε"]
            ],
            "VAR": [
                ["TIPO", "IDENTIFIER", ";"]
            ],
            "METODO": [
                ["public", "TIPO", "IDENTIFIER", "(", "PARAMS", ")", "{", "VAR_LIST", "CMD_LIST", "return", "EXP", ";", "}"]
            ],
            "PARAMS": [
                ["PARAM", "PARAM_LIST"], 
                ["ε"]
            ],
            "PARAM": [
                ["TIPO", "IDENTIFIER"]
            ],
            "PARAM_LIST": [
                [",", "PARAM", "PARAM_LIST"], 
                ["ε"]
            ],
            "TIPO": [
                ["int", "TIPO_TAIL"],
                ["boolean"],
                ["IDENTIFIER"]
            ],
            "TIPO_TAIL": [
                ["[", "]"],
                ["ε"]
            ],
            "CMD_LIST": [
                ["CMD", "CMD_LIST"],
                ["ε"]
            ],
            "CMD": [
                ["{", "CMD_LIST", "}"],
                ["if", "(", "EXP", ")", "CMD", "CMD_ELSE"],
                ["while", "(", "EXP", ")", "CMD"],
                ["System.out.println", "(", "EXP", ")", ";"],
                ["IDENTIFIER", "CMD_ID"]
            ],
            "CMD_ELSE": [
                ["else", "CMD"], 
                ["ε"]
            ],
            "CMD_ID": [
                ["=", "EXP", ";"], 
                ["[", "EXP", "]", "=", "EXP", ";"]
            ],
            "EXP": [
                ["REXP", "EXP_TAIL"]
            ],
            "EXP_TAIL": [
                ["&&", "REXP", "EXP_TAIL"], 
                ["ε"]
            ],
            "REXP": [
                ["AEXP", "REXP_TAIL"]
            ],
            "REXP_TAIL": [
                ["<", "AEXP"], 
                ["==", "AEXP"], 
                ["!=", "AEXP"], 
                ["ε"]
            ],
            "AEXP": [
                ["MEXP", "AEXP_TAIL"]
            ],
            "AEXP_TAIL": [
                ["+", "MEXP", "AEXP_TAIL"], 
                ["-", "MEXP", "AEXP_TAIL"], 
                ["ε"]
            ],
            "MEXP": [
                ["SEXP", "MEXP_TAIL"]
            ],
            "MEXP_TAIL": [
                ["*", "SEXP", "MEXP_TAIL"], 
                ["ε"]
            ],
            "SEXP": [
                ["!", "SEXP"],
                ["-", "SEXP"],
                ["true"],
                ["false"],
                ["NUMBER"],
                ["null"],
                ["new", "int", "[", "EXP", "]"],
                ["PEXP", "SEXP_TAIL"]
            ],
            "SEXP_TAIL": [
                [".", "length"],
                ["[", "EXP", "]"],
                ["ε"]
            ],
            "PEXP": [
                ["IDENTIFIER", "PEXP_TAIL"],
                ["this"],
                ["new", "IDENTIFIER", "(", ")"],
                ["(", "EXP", ")"]
            ],
            "PEXP_TAIL": [
                [".", "IDENTIFIER", "PEXP_TAIL_TAIL"],
                ["ε"]
            ],
            "PEXP_TAIL_TAIL": [
                ["PEXP_TAIL"],
                ["(", "EXPS", ")"]
            ],
            "EXPS": [
                ["EXP", "EXPS_LIST"], 
                ["ε"]
            ],
            "EXPS_LIST": [
                [",", "EXP", "EXPS_LIST"], 
                ["ε"]
            ]
        }

        self.current = 0

    def current_token(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]

    def consume(self, expected_value=None):
        token = self.current_token()

        if token is None:
            raise ParserError(f"Unexpected end of input, expected {expected_value}")

        if token.value is None:
            raise ParserError(f"Unexpected end of input, expected {expected_value}")

        if expected_value and expected_value != 'IDENTIFIER' and token.value != expected_value:
            raise ParserError(f"Expected {expected_value}, got {token.value}")

        self.current += 1
        return token

    def parse_rule(self, rule_name):
        print(f"Rule: {rule_name}")
        rules = self.grammar[rule_name]
        for rule in rules:
            state = self.current
            try:
                return self.match_sequence(rule)
            except ParserError:
                self.current = state
        raise ParserError(f"Failed to match rule: {rule_name}")

    def match_sequence(self, sequence):
        children = []
        # children.append(sequence)
        for element in sequence:
            print(f"Element: {element}")
            if isinstance(element, list):
                try:
                    children.append(self.match_sequence(element))
                except ParserError:
                    continue
            elif element in self.grammar:  # Não terminal
                children.append(self.parse_rule(element))
            else:  # Terminal
                children.append(self.consume(expected_value=element).value)
        return children

    def parse(self):
        return self.parse_rule("PROG")
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
from scanner import Scanner


class ParserError(Exception):
    pass


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.grammar = {
            "PROG": [["MAIN", "CLASSE_LIST"]],
            "CLASSE_LIST": [["CLASSE", "CLASSE_LIST"], []],
            "MAIN": [
            ["class", "IDENTIFIER", "{", "public", "static", "void", "main",
             "(", "String", "[", "]", "IDENTIFIER", ")", "{", "CMD_LIST", "}", "}"]
            ],
            "CLASSE": [
            ["class", "IDENTIFIER", "CLASSE_EXT", "{", "VAR_LIST", "METODO_LIST", "}"]
            ],
            "CLASSE_EXT": [["extends", "IDENTIFIER"], []],
            "VAR_LIST": [["VAR", "VAR_LIST"], []],
            "METODO_LIST": [["METODO", "METODO_LIST"], []],
            "VAR": [["TIPO", "IDENTIFIER", ";"]],
            "METODO": [
            ["public", "TIPO", "IDENTIFIER", "(", "PARAMS", ")", "{", "VAR_LIST", "CMD_LIST", "return", "EXP", ";", "}"]
            ],
            "PARAMS": [["PARAM", "PARAM_LIST"], []],
            "PARAM": [["TIPO", "IDENTIFIER"]],
            "PARAM_LIST": [[",", "PARAM", "PARAM_LIST"], []],
            "TIPO": [
            ["int", "[", "]"],
            ["boolean"],
            ["int"],
            ["IDENTIFIER"]
            ],
            "CMD_LIST": [["CMD", "CMD_LIST"], []],
            "CMD": [
            ["{", "CMD_LIST", "}"],
            ["if", "(", "EXP", ")", "CMD", "CMD_ELSE"],
            ["while", "(", "EXP", ")", "CMD"],
            ["System.out.println", "(", "EXP", ")", ";"],
            ["IDENTIFIER", "CMD_ID"]
            ],
            "CMD_ELSE": [["else", "CMD"], []],
            "CMD_ID": [["=", "EXP", ";"], ["[", "EXP", "]", "=", "EXP", ";"]],
            "EXP": [["REXP", "EXP_TAIL"]],
            "EXP_TAIL": [["&&", "REXP", "EXP_TAIL"], []],
            "REXP": [["AEXP", "REXP_TAIL"]],
            "REXP_TAIL": [["<", "AEXP"], ["==", "AEXP"], ["!=", "AEXP"], []],
            "AEXP": [["MEXP", "AEXP_TAIL"]],
            "AEXP_TAIL": [["+", "MEXP", "AEXP_TAIL"], ["-", "MEXP", "AEXP_TAIL"], []],
            "MEXP": [["SEXP", "MEXP_TAIL"]],
            "MEXP_TAIL": [["*", "SEXP", "MEXP_TAIL"], []],
            "SEXP": [
            ["!", "SEXP"],
            ["-", "SEXP"],
            ["true"],
            ["false"],
            ["NUMBER"],
            ["null"],
            ["new", "int", "[", "EXP", "]"],
            ["PEXP", ".", "length"],
            ["PEXP", "[", "EXP", "]"],
            ["PEXP"]
            ],
            "PEXP": [
            ["IDENTIFIER", "PEXP_TAIL"],
            ["this"],
            ["new", "IDENTIFIER", "(", ")"],
            ["(", "EXP", ")"]
            ],
            "PEXP_TAIL": [[".", "IDENTIFIER", "PEXP_TAIL"], [".", "IDENTIFIER", "(", "EXPS", ")"], []],
            "EXPS": [["EXP", "EXPS_LIST"], []],
            "EXPS_LIST": [[",", "EXP", "EXPS_LIST"], []],
        }

        self.current = 0

    def current_token(self):
        return self.tokens[self.current] if self.current < len(self.tokens) else None

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


# Example usage
if __name__ == "__main__":
    code = """
class Factorial {
public static void main(String[] args) {
System.out.println(10);
}
}
"""

    scanner = Scanner()
    tokens = scanner.scan(code)

    parser = Parser(tokens)
    try:
        tree = parser.parse()
        print("Parse successful:", tree)
    except ParserError as e:
        print(e)

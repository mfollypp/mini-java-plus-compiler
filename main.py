import re
from graphviz import Digraph

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children if children is not None else []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"Node({self.value}, children={self.children})"


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
                [""]
            ],
            "MAIN": [
                ["class", "IDENTIFIER", "{", "public", "static", "void", "main", "(", "String", "[", "]", "IDENTIFIER", ")", "{", "CMD_LIST", "}", "}"]
            ],
            "CLASSE": [
                ["class", "IDENTIFIER", "CLASSE_EXT", "{", "VAR_LIST", "METODO_LIST", "}"]
            ],
            "CLASSE_EXT": [
                ["extends", "IDENTIFIER"], 
                [""]
            ],
            "VAR_LIST": [
                ["VAR", "VAR_LIST"],
                [""]
            ],
            "METODO_LIST": [
                ["METODO", "METODO_LIST"], 
                [""]
            ],
            "VAR": [
                ["TIPO", "IDENTIFIER", ";"]
            ],
            "METODO": [
                ["public", "TIPO", "IDENTIFIER", "(", "PARAMS", ")", "{", "VAR_LIST", "CMD_LIST", "return", "EXP", ";", "}"]
            ],
            "PARAMS": [
                ["PARAM", "PARAM_LIST"], 
                [""]
            ],
            "PARAM": [
                ["TIPO", "IDENTIFIER"]
            ],
            "PARAM_LIST": [
                [",", "PARAM", "PARAM_LIST"], 
                [""]
            ],
            "TIPO": [
                ["int", "TIPO_TAIL"],
                ["boolean"],
                ["IDENTIFIER"]
            ],
            "TIPO_TAIL": [
                ["[", "]"],
                [""]
            ],
            "CMD_LIST": [
                ["CMD", "CMD_LIST"],
                [""]
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
                [""]
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
                [""]
            ],
            "REXP": [
                ["AEXP", "REXP_TAIL"]
            ],
            "REXP_TAIL": [
                ["<", "AEXP"], 
                ["==", "AEXP"], 
                ["!=", "AEXP"], 
                [""]
            ],
            "AEXP": [
                ["MEXP", "AEXP_TAIL"]
            ],
            "AEXP_TAIL": [
                ["+", "MEXP", "AEXP_TAIL"], 
                ["-", "MEXP", "AEXP_TAIL"], 
                [""]
            ],
            "MEXP": [
                ["SEXP", "MEXP_TAIL"]
            ],
            "MEXP_TAIL": [
                ["*", "SEXP", "MEXP_TAIL"], 
                [""]
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
                [""]
            ],
            "PEXP": [
                ["IDENTIFIER", "PEXP_TAIL"],
                ["this", "PEXP_TAIL"],
                ["new", "IDENTIFIER", "(", ")", "PEXP_TAIL"],
                ["(", "EXP", ")", "PEXP_TAIL"]
            ],
            "PEXP_TAIL": [
                [".", "IDENTIFIER", "PEXP_TAIL_TAIL"],
                [""]
            ],
            "PEXP_TAIL_TAIL": [
                ["(", "EXPS", ")", "PEXP_TAIL"],
                ["PEXP_TAIL"],
            ],
            "EXPS": [
                ["EXP", "EXPS_LIST"], 
                [""]
            ],
            "EXPS_LIST": [
                [",", "EXP", "EXPS_LIST"], 
                [""]
            ]
        }

        self.current = 0

    def current_token(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]

    def consume(self, expected_value=None, rule=None):
        token = self.current_token()
                
        if expected_value == "":
            return None
        
        if token is None:
            raise ParserError(f"Unexpected end of input, expected {expected_value}")

        if token.value is None:
            raise ParserError(f"Unexpected end of input, expected {expected_value}")

        if not expected_value:
            return None

        if expected_value not in ['IDENTIFIER', 'NUMBER'] and token.value != expected_value:
            raise ParserError(f"Expected {expected_value}, got {token.value}")
        
        if (expected_value == 'IDENTIFIER' and token.kind != 'IDENTIFIER') or (expected_value == 'NUMBER' and token.kind != 'NUMBER'):
            raise ParserError(f"Expected {expected_value}, got {token.value}")
        
        print(f"Consuming token with value: {token.value} with kind {token.kind}) (Expected: {expected_value}. Current token: {self.current})")

        self.current += 1
        return token

    def parse_rule(self, rule_name):
        print(f"Rule: {rule_name}")
        rules = self.grammar[rule_name]
        for rule in rules:
            state = self.current
            try:
                node = Node(rule_name)
                node.add_child(self.match_sequence(rule))
                return node
            except ParserError as e:
                self.current = state
                print(e)
                print(f"Heading back to grammar rule: {rule_name}")
        raise ParserError(f"Failed to match rule: {rule_name}")

    def match_sequence(self, sequence):
        root = Node("sequence")
        for element in sequence:
            print(f"Element: {element}")
            if isinstance(element, list):
                try:
                    child_node = self.match_sequence(element)
                    if child_node.children:  # Evita adicionar nós vazios
                        root.add_child(child_node)
                except ParserError:
                    continue
            elif element in self.grammar:  # Não terminal
                child_node = self.parse_rule(element)
                if child_node:
                    root.add_child(child_node)
            else:  # Terminal
                resp = self.consume(expected_value=element, rule=sequence)
                if resp is not None:
                    root.add_child(Node(resp.value))
        return root

    def parse(self):
        return self.parse_rule("PROG")
# endregion Parser


def print_ast(node, indent=0):
    print(' ' * indent + str(node.value))
    for child in node.children:
        print_ast(child, indent + 2)


def ast_to_graphviz(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='box')

    node_id = str(id(node))
    graph.node(node_id, label=str(node.value))

    if parent is not None:
        graph.edge(parent, node_id)

    for child in node.children:
        ast_to_graphviz(child, graph, node_id)

    return graph

# Example usage
if __name__ == "__main__":

#     code = """
# class Factorial{
#     public static void main(String[] a){
#         System.out.println(new Fac().ComputeFac(10));
#     }
# }
#     """

    code = """
    class Factorial{ 
        public static void main(String[] a){ 
            System.out.println(new Fac().ComputeFac(10)); 
        } 
    }

    class Fac { 
        public int ComputeFac(int num){ 
            int num_aux; 
            if (num < 1) 
                num_aux = 1; 
            else  
                num_aux = num * (this.ComputeFac(num-1)); 
            return num_aux ; 
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
        parsed_code = parser.parse()
        print("Parse successful:", parsed_code)
    except ParserError as e:
        print(e)

    # Generate and visualize the AST using graphviz
    graph = ast_to_graphviz(parsed_code)
    graph.render('ast', format='png', view=True)
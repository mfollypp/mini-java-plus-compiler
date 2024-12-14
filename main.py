import re
from graphviz import Digraph
from grammar import grammar


class Node:
    def __init__(self, value=None, children=None, terminal=False):
        self.value = value
        self.children = children if children is not None else []
        self.terminal = terminal


class Token:
    def __init__(self, kind, value, line, column):
        self.kind = kind
        self.value = value
        self.line = line
        self.column = column


class Scanner:
    def __init__(self):
        self.token_specification = [
            ('WHITESPACE',     r'[\n\t\r\f\s]+'),
            ('COMMENT',        r'//.*?$|/\*.*?\*/'), 
            ('RESERVED',       r'(boolean|class|extends|public|static|void|main|String|return|int|if|else|while|System\.out\.println|length|true|false|this|new|null)'),
            ('IDENTIFIER',     r'[a-zA-Z][a-zA-Z0-9_]*'),
            ('NUMBER',         r'\b\d+\b'), 
            ('OPERATOR',       r'\(|\)|\[|\]|\{|\}|;|\.|,|=|<|>|>=|<=|==|!=|\+|-|\*|&&|!'), 
        ]

        self.regex = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_specification)) # Usa grupo de captura -> funciona da esquerda para direita
        
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


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.grammar = grammar
        self.current = 0

    def current_token(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]

    def consume(self, expected_value=None, rule=None):
        token = self.current_token()
                
        if expected_value == "":
            return None
        
        if token is None:
            raise Exception(f"Unexpected end of input, expected {expected_value}")

        if token.value is None:
            raise Exception(f"Unexpected end of input, expected {expected_value}")

        if not expected_value:
            return None

        if expected_value not in ['IDENTIFIER', 'NUMBER'] and token.value != expected_value:
            raise Exception(f"Expected {expected_value}, got {token.value}")
        
        if (expected_value == 'IDENTIFIER' and token.kind != 'IDENTIFIER') or (expected_value == 'NUMBER' and token.kind != 'NUMBER'):
            raise Exception(f"Expected {expected_value}, got {token.value}")
        
        print(f"- Consuming token with value: {token.value} \n- with kind {token.kind}\n- Expected: '{expected_value}'\n- Current token: {self.current}")

        self.current += 1
        return token

    def parse_rule(self, rule_name):
        print(f"Rule: {rule_name}")
        rules = self.grammar[rule_name]
        for rule in rules:
            state = self.current
            try:
                return self.match_sequence(rule, rule_name)
            except Exception as e:
                self.current = state
                print(e)
                print(f"Heading back to grammar rule: {rule_name}")
        raise Exception(f"Failed to match rule: {rule_name}")

    def match_sequence(self, sequence, rule_name):
        root = Node(rule_name)
        for element in sequence:
            print(f"Element: {element}")
            if element in self.grammar:  # Não terminal
                child_node = self.parse_rule(element)
                if child_node:
                    root.children.append(child_node)
            else:  # Terminal
                resp = self.consume(expected_value=element, rule=sequence)
                if resp is not None:
                    root.children.append(Node(resp.value, terminal=True))
        return root

    def parse(self):
        response = self.parse_rule("PROG")
        if self.current < len(self.tokens):
            raise Exception(f"Did not finish parsing, still have {len(self.tokens) - self.current} tokens left")
        return response
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
    if node.terminal:  # Se o nó é terminal, pinte com fundo amarelo
        graph.node(node_id, label=str(node.value), style='filled', fillcolor='yellow')
    else:
        graph.node(node_id, label=str(node.value))

    if parent is not None:
        graph.edge(parent, node_id)

    for child in node.children:
        ast_to_graphviz(child, graph, node_id)

    return graph


if __name__ == "__main__":

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
        print("\nParse successful!!\n")
        graph = ast_to_graphviz(parsed_code)
        graph.render('ast', format='png', view=True)
    except Exception as e:
        print(e)
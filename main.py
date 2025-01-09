from graphviz import Digraph
from grammar import grammar
import re


class Node:
    def __init__(self, value=None, children=None, terminal=False, kind=None, parent=None, line=None, column=None):
        self.value = value
        self.children = children if children is not None else []
        self.terminal = terminal
        self.kind = kind
        self.parent = parent
        self.line = line
        self.column = column


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
        line = 0
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
                value = int(value)

            token = Token(kind, value, line, column)
            tokens.append(token)

        return tokens


class Parser:
    def __init__(self, tokens, parser_steps):
        self.tokens = tokens
        self.grammar = grammar
        self.current = 0
        self.parser_steps = parser_steps

    def current_token(self):
        if self.current < len(self.tokens):
            return self.tokens[self.current]

    def consume(self, expected_value=None, rule_name=None):
        token = self.current_token()
                
        if expected_value == "": # epsilon
            return None
        
        if token is None or token.value is None:
            parser_steps.write(f"\nUnexpected end of input, expected `{expected_value}`")
            raise Exception(f"Unexpected end of input, expected {expected_value}")

        if expected_value not in ['IDENTIFIER', 'NUMBER'] and token.value != expected_value:
            parser_steps.write(f"\nExpected production element:`{expected_value}`, but current token is:`{token.value}`")
            raise Exception(f"Expected '{expected_value}', got '{token.value}'")
        
        if (expected_value == 'IDENTIFIER' and token.kind != 'IDENTIFIER') or (expected_value == 'NUMBER' and token.kind != 'NUMBER'):
            parser_steps.write(f"\nExpected production element:`{expected_value}`, but current token is:`{token.value}`")
            raise Exception(f"Expected '{expected_value}', got '{token.value}'")
        
        parser_steps.write(f"\n- Consuming token with value: `{token.value}` and kind: `{token.kind}` (consumed inside production: `{rule_name}`) \
                           \n- Expected token with value: `{expected_value}` \
                           \n- Current token index: {self.current}")

        self.current += 1
        return token

    def parse_rule(self, rule_name):
        parser_steps.write(f"\n\nProduction: `{rule_name}` ")
        rules = self.grammar[rule_name]
        for rule in rules:
            state = self.current
            try:
                return self.match_sequence(rule, rule_name)
            except Exception as e:
                self.current = state
                print(e)
                parser_steps.write(f"\n- Heading back to grammar production: `{rule_name}`")
        raise Exception(f"Failed to match rule: {rule_name}")

    def match_sequence(self, sequence, rule_name):
        root = Node(rule_name)
        parser_steps.write(f' ->  `{sequence}`\n')
        for element in sequence:
            if element == "":  # epsilon
                parser_steps.write(f'\n\nAnalyzing Element: `""` of production\n')
            else:
                parser_steps.write(f"\n\nAnalyzing Element: `{element}` of production\n")
            if element in self.grammar:  # Não terminal
                child_node = self.parse_rule(element)
                if child_node:
                    root.children.append(child_node)
            else:  # Terminal
                token_resp = self.consume(element, rule_name)
                if token_resp is not None:
                    root.children.append(
                        Node(
                            value=token_resp.value, 
                            terminal=True, 
                            kind=token_resp.kind, 
                            parent=root, 
                            line=token_resp.line, 
                            column=token_resp.column
                        )
                    )
        parser_steps.write(f"\n- Exiting grammar production: `{rule_name}`")
        return root

    def parse(self):
        response = self.parse_rule("PROG")
        if self.current < len(self.tokens):
            raise Exception(f"Did not finish parsing, still have {len(self.tokens) - self.current} tokens left")
        return response
    
class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = {}
        self.highlighted_nodes = set()

    def analyze(self, node):
        print(f"Analyzing node: {node.value}, of kind: {node.kind} with parent: {node.parent.value if node.parent else None}")

        if node.kind == "IDENTIFIER":
            if node.parent.value == "CLASSE" or node.parent.value == "METODO" or node.parent.value == "MAIN":
                var_name = node.value
                self.symbol_table[var_name] = node.parent.kind

        for child in node.children:
            self.analyze(child)

    def analyze2(self, node):
        print(f"Analyzing node: {node.value}, of kind: {node.kind} with parent: {node.parent.value if node.parent else None}")

        if node.kind == "IDENTIFIER":
            if node.parent.value == "VAR" or node.parent.value == "PARAM":
                var_name = node.value
                self.symbol_table[var_name] = node.parent.kind
            else:
                var_name = node.value
                if var_name not in self.symbol_table:
                    raise Exception(f"[Error]: Variable '{var_name}' used before declaration in line {node.line} column {node.column}")
                
        print(f"Symbol Table: {self.symbol_table}\n")
        
        for child in node.children:
            self.analyze2(child)

    def fold_constants(self, node):
        if node.terminal:
            return node
        
        for child in node.children:
            self.fold_constants(child)
        
        if node.value == "EXP":
            terminals = []
            self.collect_terminals(node, terminals)
            if all(term.kind == "NUMBER" or term.kind == "OPERATOR" for term in terminals):
                expression = " ".join(str(term.value) for term in terminals)
                print(f"\nExpression: {expression}\n")
                try:
                    result = eval(expression)
                    node.value = str(result)
                    node.children = []
                    node.terminal = True
                    self.highlighted_nodes.add(node)
                except Exception as e:
                    print(f"Failed to evaluate expression: {expression}. Error: {e}")
        
        return node, self.highlighted_nodes

    def collect_terminals(self, node, terminals):
        print(f"Collecting terminals for node: {node.value} (Terminal: {node.terminal}) with children: {[child.value for child in node.children]}")
        if node.terminal:
            terminals.append(node)
        for child in node.children:
            self.collect_terminals(child, terminals)


def ast_to_graphviz(node, graph=None, parent=None, highlighted_nodes=None):
    if graph is None:
        graph = Digraph()
        graph.attr('node', shape='box')

    node_id = str(id(node))
    if highlighted_nodes and node in highlighted_nodes:
        print(f"Highlighting node: {node.value} with color green")
        graph.node(node_id, label=str(node.value), style='filled', fillcolor='green')
    elif node.terminal:
        graph.node(node_id, label=str(node.value), style='filled', fillcolor='yellow')
    else:
        graph.node(node_id, label=str(node.value))

    if parent is not None:
        graph.edge(parent, node_id)

    for child in node.children:
        ast_to_graphviz(child, graph, node_id, highlighted_nodes)

    return graph


if __name__ == "__main__":

    # num_aux = (1 + 2) * 2; não funciona corretamente, da 3, mas se tirar os parênteses da 5, o eval não ta certinho
    code = """
    class Factorial{ 
        public static void main(String[] a){ 
            System.out.println(new Fac().ComputeFac(10));
        } 
    }
    class Fac { 
        public int ComputeFac(int num){
            int num_aux ;
            if (num < 1) 
                num_aux = 1 + 2; 
            else  
                num_aux = num * (this.ComputeFac(num-1)); 
            return num_aux ; 
        } 
    }
    """
    print(f"\nScanning code:\n{code}\n")
    
    parser_steps = open('parser_steps.md', 'w')

    with open('scanned_tokens.md', 'w') as scanned_tokens:
        scanner = Scanner()
        tokens = scanner.scan(code)

        for token in tokens:
            scanned_tokens.write(f"\n`{token.kind}`: `{token.value}` at line {token.line}, column {token.column}\n")

    try:
        with open('parser_steps.md', 'w') as parser_steps:
            parser = Parser(tokens, parser_steps)
            parsed_code = parser.parse()
        print("\nParse successful!!\n")
        graph = ast_to_graphviz(parsed_code)
        graph.render('ast', format='png', view=False)

        # Semantic Analysis
        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.analyze(parsed_code) # Primeira passada
        semantic_analyzer.analyze2(parsed_code) # Segunda passada

        # Substituição de expressões com constantes pelo seu valor numérico
        parsed_code, highlighted_nodes = semantic_analyzer.fold_constants(parsed_code)
        print("Highlighted nodes: ", highlighted_nodes)

        graph_semantic = ast_to_graphviz(parsed_code, highlighted_nodes=highlighted_nodes)
        graph_semantic.render('ast_semantic', format='png', view=False)
        print("\nSemantic analysis successful!!\n")
    except Exception as e:
        print(e)
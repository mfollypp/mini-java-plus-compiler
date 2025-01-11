from graphviz import Digraph
from grammar import grammar
import re
import copy

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
                    child_node.parent = root
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
        
    def build_name(self, node):
        method_name = ""
        class_name = ""
        node_aux = copy.copy(node)
        
        while node_aux and node_aux.value and node_aux.value != "METODO":
            node_aux = node_aux.parent
        
        if(not node_aux):
            return node.value
        
        method_name = node_aux.children[2].value  
        
        while node_aux and node_aux.value and node_aux.value != "CLASSE":
            node_aux = node_aux.parent        
            
        if (not node_aux):
            return node.value
            
        class_name = node_aux.children[1].value  
        
        if(class_name and method_name):
            return f"{class_name}_{method_name}_{node.value}"
        else:
            return node.value

    def analyze(self, node):
        print(f"Analyzing node: {node.value}, of kind: {node.kind} with parent: {node.parent.value if node.parent else None}")

        if node.kind == "IDENTIFIER":
            if node.parent.value == "CLASSE" or node.parent.value == "METODO" or node.parent.value == "MAIN":
                var_name = node.value
                self.symbol_table[var_name] = "method_class"

        for child in node.children:
            self.analyze(child)

    def analyze2(self, node):
        print(f"Analyzing node: {node.value}, of kind: {node.kind} with parent: {node.parent.value if node.parent else None}")

        if node.kind == "IDENTIFIER":
            if node.parent.value == "VAR" or node.parent.value == "PARAM":
                var_name = self.build_name(node)                
                    
                if var_name in self.symbol_table:
                    raise Exception(f"Variable '{node.value}' already declared in scope.")
                self.symbol_table[var_name] = node.parent.kind
                node.value = var_name
            elif node.parent.value != "MAIN":
                if node.value in self.symbol_table and self.symbol_table[node.value] == "method_class":
                    pass
                else:
                    var_name = self.build_name(node)
                    if var_name not in self.symbol_table:
                        raise Exception(f"Variable '{var_name}' not declared in symbol table")
                    node.value = var_name
                
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
                    if(result == False):
                        result = 0
                    elif (result == True):
                        result = 1
                    result_child = Node(str(result), terminal=True, kind="NUMBER")
                    node.children = [result_child]
                    self.highlighted_nodes.add(result_child)
                except Exception as e:
                    print(f"Failed to evaluate expression: {expression}. Error: {e}")
        
        return node, self.highlighted_nodes

    def collect_terminals(self, node, terminals):
        print(f"Collecting terminals for node: {node.value} (Terminal: {node.terminal}) with children: {[child.value for child in node.children]}")
        if node.terminal:
            terminals.append(node)
        for child in node.children:
            self.collect_terminals(child, terminals)


class MIPSCodeGenerator:
    def __init__(self):
        self.code = []
        self.temp_count = 0
        self.variable_map = {}
        self.method_map = {}

    def generate_code(self, node):
        
        print(node.value, node.terminal, node.kind, len(node.children))
        
        """Gera código MIPS a partir da AST."""
        if node.value == "PROG":
            # Programa: desce para o MAIN e as classes
            for child in node.children:
                self.generate_code(child)

        elif node.value == "MAIN":
            # MAIN: Configura o ponto de entrada
            self.code.append(".text")
            self.code.append("main:")
            for child in node.children:
                self.generate_code(child)
            self.code.append("li $v0, 10")
            self.code.append("syscall")

        elif node.value in ["CLASSE_LIST", "CLASSE", "VAR_LIST", "METODO_LIST"]:
            for child in node.children:
                self.generate_code(child)

        elif node.value == "VAR":
            # Variável: gera um rótulo para a variável
            var_name = node.children[1].value
            if var_name not in self.variable_map:
                self.variable_map[var_name] = f"{var_name}: .word 0"
                if ".data" not in self.code:
                    self.code.insert(0, ".data")
                self.code.insert(1, self.variable_map[var_name])
                
        elif node.value == "METODO":
            # Método: gera um rótulo para o método
            method_name = node.children[2].value
            self.method_map[method_name] = method_name
            self.code.append(f"{method_name}:")
            for child in node.children:
                self.generate_code(child)
            self.code.append("jr $ra")

        elif node.value == "CMD_LIST":
            # Lista de comandos
            for child in node.children:
                self.generate_code(child)

        elif node.value == "CMD":
            if len(node.children) == 3:
                self.generate_code(node.children[1])
                # expr_reg = self.generate_code(node.children[2])
                # if var_name not in self.variable_map:
                #     self.variable_map[var_name] = f"{var_name}: .word 0"
                #     if ".data" not in self.code:
                #         self.code.insert(0, ".data")
                #     self.code.insert(1, self.variable_map[var_name])
                # self.code.append(f"sw {expr_reg}, {self.variable_map[var_name]}")

            elif len(node.children) == 6 and node.children[0].value == "if":
                expr_reg = self.generate_code(node.children[2])
                label_count = self.temp_count
                label = f"else_{label_count}"
                self.code.append(f"beq {expr_reg}, $zero, {label}")
                self.generate_code(node.children[4])
                self.code.append(f"j end_if_{label_count}")
                self.code.append(f"{label}:")
                self.generate_code(node.children[5])
                self.code.append(f"end_if_{label_count}:")
                self.temp_count += 1
                
            elif len(node.children) == 5 and node.children[0].value == "while":
                label = f"while_{self.temp_count}"
                self.code.append(f"{label}:")
                expr_reg = self.generate_code(node.children[2])
                end_label = f"end_while_{self.temp_count}"
                self.code.append(f"beq {expr_reg}, $zero, {end_label}")
                self.generate_code(node.children[4])
                self.code.append(f"j {label}")
                self.code.append(f"{end_label}:")
                self.temp_count += 1

            elif len(node.children) == 5 and node.children[0].value == "System.out.println":
                expr_reg = self.generate_code(node.children[2])
                self.code.append(f"move $a0, {expr_reg}")
                self.code.append("li $v0, 1")
                self.code.append("syscall")
                
            elif len(node.children) == 2:
                self.generate_code(node.children[1])
                
        elif node.value == "CMD_ELSE":
            if len(node.children) == 2:
                self.generate_code(node.children[1])
        
        elif node.value == "CMD_ID":
            if len(node.children) == 3:
                var_name = node.children[0].value
                expr_reg = self.generate_code(node.children[2])
                if var_name not in self.variable_map:
                    self.variable_map[var_name] = f"{var_name}: .word 0"
                    if ".data" not in self.code:
                        self.code.insert(0, ".data")
                    self.code.insert(1, self.variable_map[var_name])
                self.code.append(f"sw {expr_reg}, {self.variable_map[var_name]}")
            elif len(node.children) == 5:
                var_name = node.children[0].value
                expr_reg = self.generate_code(node.children[4])
                index_reg = self.generate_code(node.children[2])
                if var_name not in self.variable_map:
                    self.variable_map[var_name] = f"{var_name}: .word 0"
                    if ".data" not in self.code:
                        self.code.insert(0, ".data")
                    self.code.insert(1, self.variable_map[var_name])
                self.code.append(f"sw {expr_reg}, {self.variable_map[var_name]}({index_reg})")

        elif node.value == "EXP":
            if node.children[0].kind == "NUMBER":
                reg = self.get_temp_register()
                self.code.append(f"li {reg}, {node.children[0].value}")
                return reg
            return self.generate_code(node.children[0])

        elif node.value == "REXP":
            return self.generate_code(node.children[0])

        elif node.value == "AEXP":
            left = self.generate_code(node.children[0])
            if len(node.children) > 2:
                operator = node.children[1].value
                right = self.generate_code(node.children[2])
                reg = self.get_temp_register()
                if operator == "+":
                    self.code.append(f"add {reg}, {left}, {right}")
                elif operator == "-":
                    self.code.append(f"sub {reg}, {left}, {right}")
                return reg
            return left
        
        elif node.value == "PEXP":
            if node.children[0].value == "IDENTIFIER":
                var_name = node.children[0].value
                if var_name not in self.variable_map:
                    self.variable_map[var_name] = f"{var_name}: .word 0"
                    if ".data" not in self.code:
                        self.code.insert(0, ".data")
                    self.code.insert(1, self.variable_map[var_name])
                reg = self.get_temp_register()
                self.code.append(f"lw {reg}, {self.variable_map[var_name]}")
                return reg
            elif node.children[0].value == "NUMBER":
                reg = self.get_temp_register()
                self.code.append(f"li {reg}, {node.children[0].value}")
                return reg

        elif node.value == "MEXP":
            left = self.generate_code(node.children[0])
            if len(node.children) > 2:
                operator = node.children[1].value
                right = self.generate_code(node.children[2])
                reg = self.get_temp_register()
                if operator == "*":
                    self.code.append(f"mul {reg}, {left}, {right}")
                return reg
            return left

        elif node.value == "SEXP":
            if len(node.children) == 1 and node.children[0].terminal:
                if node.children[0].kind == "NUMBER":
                    reg = self.get_temp_register()
                    self.code.append(f"li {reg}, {node.children[0].value}")
                    return reg
                elif node.children[0].value == "true":
                    reg = self.get_temp_register()
                    self.code.append(f"li {reg}, 1")
                    return reg
                elif node.children[0].value == "false":
                    reg = self.get_temp_register()
                    self.code.append(f"li {reg}, 0")
                    return reg
                elif node.children[0].value == "null":
                    reg = self.get_temp_register()
                    self.code.append(f"li {reg}, 0")
                    return reg
            elif len(node.children) == 2:
                if node.children[0].value == "!":
                    reg = self.generate_code(node.children[1])
                    self.code.append(f"not {reg}, {reg}")
                    return reg
                elif node.children[0].value == "-":
                    reg = self.generate_code(node.children[1])
                    self.code.append(f"neg {reg}, {reg}")
                    return reg
            elif len(node.children) == 5 and node.children[0].value == "new" and node.children[1].value == "int":
                reg_size = self.generate_code(node.children[3])
                reg = self.get_temp_register()
                self.code.append(f"li {reg}, {reg_size}")
                self.code.append(f"mul {reg}, {reg}, 4")  # Assuming int is 4 bytes
                self.code.append(f"li $v0, 9")  # Syscall for sbrk
                self.code.append(f"move $a0, {reg}")
                self.code.append(f"syscall")
                self.code.append(f"move {reg}, $v0")
                return reg
            elif len(node.children) == 2 and node.children[1].value == "SEXP_1":
                reg = self.generate_code(node.children[0])
                reg_sexp1 = self.generate_code(node.children[1])
                self.code.append(f"add {reg}, {reg}, {reg_sexp1}")
                return reg

        # Caso o nó não produza código
        return None

    def get_temp_register(self):
        reg = f"$t{self.temp_count}"
        self.temp_count = (self.temp_count + 1) % 10
        return reg

    def write_code(self, filename):
        print(f"\nCode: {self.code}\n")
        if not self.code:
            self.code = [".data", ".text", "main:"]
        with open(filename, "w") as f:
            f.write("\n".join(self.code))


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

    code = """
    class Factorial{ 
        public static void main(String[] a){ 
            System.out.println(new Fac().ComputeFac(10));
        } 
    }
    class Fac { 
        public int ComputeFac(int num){
            return 10;
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
        parsed_code_semantic, highlighted_nodes = semantic_analyzer.fold_constants(parsed_code)
        print("Highlighted nodes: ", highlighted_nodes)

        graph_semantic = ast_to_graphviz(parsed_code_semantic, highlighted_nodes=highlighted_nodes)
        graph_semantic.render('ast_semantic', format='png', view=False)
        print("\nSemantic analysis successful!!\n")

        # Geração de Código MIPS
        code_generator = MIPSCodeGenerator()
        code_generator.generate_code(parsed_code_semantic)
        code_generator.write_code("output.asm")  # Salva o código MIPS no arquivo 'output.asm'
        print("\nMIPS code generation completed! Check 'output.asm'.\n")
    except Exception as e:
        print(e)
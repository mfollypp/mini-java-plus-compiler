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
            ('ERROR',          r'.'),
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

            if kind == 'ERROR':
                raise ValueError(f"Unrecognized token '{value}' at line {line}, column {column}")
                
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
        self.method_map = {}
        self.main_identifier_count = 0
    
    def get_leaves(self, node):
        if not node.children and node.terminal:
            return [node.value]
        leaves = []
        for child in node.children:
            leaves.extend(self.get_leaves(child))
        return leaves

    def build_name(self, node):
        method_name = ""
        class_name = ""
        node_aux = copy.copy(node)
        
        if node.parent.value == "MAIN":
            value = node.value if self.main_identifier_count == 0 else f"|{next(iter(self.symbol_table))}|{node.value}"
            self.main_identifier_count += 1
            return value
                
        if(node.parent.value == "PEXP"):
            before = node.parent.children[0].value
            if before in ["new", "."]:
                return node.value

        if(node.parent.value == "CLASSE"):
            class_name = node.parent.children[1].value
            return node.value
        
        if(node.parent.value == "PEXP_1"):
            if(not class_name):
                if(node.parent.parent.children[0].value == "new"):
                    class_name = node.parent.parent.children[1].value
                else:
                    while node_aux.value != "CLASSE":
                        node_aux = node_aux.parent
                    class_name = node_aux.children[1].value
            return f"|{class_name}|{node.value}"
        
        while node_aux and node_aux.value and node_aux.value != "METODO":
            node_aux = node_aux.parent
        
        if(node_aux):
            method_name = node_aux.children[2].value.split("|")[-1]
        else:
            node_aux = node
        
        while node_aux and node_aux.value and node_aux.value != "CLASSE":
            node_aux = node_aux.parent        
            
        if (node_aux):
            class_name = node_aux.children[1].value.split("|")[0]  
                    
        if(node.parent.value in "METODO"):
            return f"|{class_name}|{method_name}"
            
        return f"|{class_name}|{method_name}|{node.value}"

    def analyze(self, node):
        print(f"Analyzing node: {node.value}, of kind: {node.kind} with parent: {node.parent.value if node.parent else None}")

        if node.kind == "IDENTIFIER":
            if node.parent.value == "CLASSE" or node.parent.value == "METODO" or node.parent.value == "MAIN":
                if(node.parent.value == "MAIN"):
                    var_name = self.build_name(node)
                elif node.parent.value == "METODO":
                    var_name = self.build_name(node)
                    params_node = node.parent.children[4]
                    terminals = self.get_leaves(params_node)
                    params = "".join(str(element) for element in terminals)
                    self.method_map[var_name] = len(params.split(","))
                else: 
                    var_name = node.value
                if var_name in self.symbol_table:
                    raise Exception(f"Variable '{self.symbol_table[var_name]}' already declared in scope.")
                self.symbol_table[var_name] = node.value
                node.value = var_name
                
        for child in node.children:
            self.analyze(child)

    def analyze2(self, node):
        print("Analyse 2")
        print(f"Analyzing node: {node.value}, of kind: {node.kind} with parent: {node.parent.value if node.parent else None}")

        if node.kind == "IDENTIFIER":
            parent = node.parent.value
            if parent in ["VAR", "PARAM"]:
                var_name = self.build_name(node)                
                if var_name in self.symbol_table:
                    raise Exception(f"Variable '{self.symbol_table[var_name]}' already declared in scope.")
                self.symbol_table[var_name] = node.value
                node.value = var_name
            elif parent not in ["MAIN", "METODO", "CLASSE"]:
                var_name = self.build_name(node)
                if var_name not in self.symbol_table:
                    raise Exception(f"Variable '{node.value}' not declared in symbol table")
                node.value = var_name
        elif node.value == "EXPS":
            terminals = self.get_leaves(node)
            params = "".join(str(element) for element in terminals)
            number_of_params = len(params.split(","))
            # nome do metodo vindo de PEXP_1
            method_name = node.parent.parent.children[1].value
            if(number_of_params != self.method_map[method_name]):
                raise Exception(f"Method '{self.symbol_table[method_name]}' expects {self.method_map[method_name]} parameters, but got {number_of_params}")
                
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
        self.stack = []
        self.num_elems = 0
        self.elements_stacks = 0
        self.method_map = {}

    def get_leaves(self, node):
        if not node.children and node.terminal:
            return [node.value]
        leaves = []
        for child in node.children:
            leaves.extend(self.get_leaves(child))
        return leaves
        
    def push_stack(self, var_name):
        self.stack.insert(0, var_name) 
        self.code.append(f"sw $a0 0($sp)")
        self.code.append(f"addiu $sp, $sp, -4")
        
    def pop_stack(self):
        self.stack.pop(0)
        self.code.append(f"addiu $sp, $sp, 4")
    
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

        elif node.value in ["CLASSE_LIST", "VAR_LIST", "METODO_LIST", "PARAMS", "PARAM_LIST"]:
            for child in node.children:
                self.generate_code(child)
                                
        elif node.value == "CLASSE":
            class_name = node.children[1].value
            self.code.append(f"{class_name}:")
            self.generate_code(node.children[4])
            self.code.append(f"jr $ra")
            self.generate_code(node.children[5])

        elif node.value in ["VAR"]:
            #todo: validacao de tipo
            var_name = node.children[1].value
            self.push_stack(var_name)
        
        elif node.value == "PARAM":
            var_name = node.children[1].value
            # self.push_stack(var_name)
            # TODO - Colocar só no dicionario do metodo e não na stack - Kevin
                    
        elif node.value == "METODO":
            # Método: gera um rótulo para o método
            method_name = node.children[2].value
            params_node = node.children[4]
            terminals = self.get_leaves(params_node)
            if "," in terminals:
                terminals.remove(",")
            self.method_map[method_name] = terminals[1::2]
            self.code.append(f"{method_name}:")
            self.code.append("move $fp $sp")
            # self.push_stack(None) # Marca movimento na stack para uso do código
            self.code.append("sw $ra 0($sp)")
            self.code.append("addiu $sp, $sp, -4")
            for child in node.children:
                self.generate_code(child)
            # self.code.append("lw $ra 4($sp)")
            # colocar popstack para limpar argumentos do método
            self.code.append("lw $fp 0($sp)")
            self.code.append("jr $ra")

        elif node.value == "CMD_LIST":
            for child in node.children:
                self.generate_code(child)

        elif node.value == "CMD":
            if len(node.children) == 3:
                self.generate_code(node.children[1])

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
                temp_count = self.temp_count
                label = f"while_{temp_count}"
                self.code.append(f"{label}:")
                expr_reg = self.generate_code(node.children[2])
                end_label = f"end_while_{temp_count}"
                self.code.append(f"beq {expr_reg}, $zero, {end_label}")
                self.generate_code(node.children[4])
                self.code.append(f"j {label}")
                self.code.append(f"{end_label}:")
                self.temp_count += 1

            elif len(node.children) == 5 and node.children[0].value == "System.out.println":
                expr_reg = self.generate_code(node.children[2])
                self.code.append("li $v0, 1")
                self.code.append("syscall")
                
            elif len(node.children) == 2:
                self.generate_code(node.children[1])
                node_aux = node
                while node_aux.value != "METODO":
                    node_aux = node_aux.parent
                method_name = node_aux.children[2].value
                var_name = node.children[0].value
                if var_name in self.method_map[method_name]:
                    offset = (self.method_map[method_name].index(var_name) + 1) * 4
                    self.code.append(f"sw $a0, {offset}($fp)")
                else:
                    offset = (self.stack.index(var_name) + 1) * 4
                    self.code.append(f"sw $a0, {offset}($sp)")
                
        elif node.value == "CMD_ELSE":
            if len(node.children) == 2:
                self.generate_code(node.children[1])
        
        elif node.value == "CMD_ID":
            if len(node.children) == 3:
                var_name = node.parent.children[0].value
                expr_reg = self.generate_code(node.children[1])
                offset = (self.stack.index(var_name) + 1) * 4
                self.code.append(f"sw {expr_reg}, {offset}($sp)")
                    
            elif len(node.children) == 5:
                expr_reg = self.generate_code(node.children[4])
                index_reg = self.generate_code(node.children[1])
                var_name = f"_{node.parent.children[0].value}_{index_reg}"
                self.push_stack(var_name)
                offset = (self.stack.index(var_name) + 1) * 4
                self.code.append(f"sw {expr_reg}, {offset}($sp)")

        elif node.value == "EXP":
            if node.children[0].kind == "NUMBER":
                reg = "$a0"
                self.code.append(f"li {reg}, {node.children[0].value}")
                return reg
            else:
                self.generate_code(node.children[0])
                resp = self.generate_code(node.children[1])
                if(not resp):
                    return "$a0"
                self.code.append(f"lw $t0 4($sp)")
                self.code.append(f"and $a0, $t0, $a0")
                return "$a0"
            
        elif node.value == "EXP_1":
            if len(node.children) == 3:
                self.push_stack(None)
                self.generate_code(node.children[1])
                resp = self.generate_code(node.children[2])
                if(not resp):
                    return "$a0"
                self.code.append(f"lw $t0 4($sp)")
                self.code.append(f"and $a0, $t0, $a0")
                return "$a0"
        
        elif node.value == "REXP":
            # AEXP
            self.generate_code(node.children[0])
            # REXP_1
            resp = self.generate_code(node.children[1])
            if resp:
                operator = node.children[1].children[0].value
                self.code.append(f"lw $t0 4($sp)")
                self.pop_stack()
                if operator == "<":
                    self.code.append(f"slt $a0, $t0, $a0")
                elif operator == "==":
                    self.code.append(f"seq $a0, $t0, $a0")
                elif operator == "!=":
                    self.code.append(f"sne $a0, $t0, $a0")
            else:
                return True
            
        elif node.value == "REXP_1":
            if len(node.children) == 2:
                self.push_stack(None)
                self.generate_code(node.children[1])
                return True

        elif node.value == "AEXP":
            # MEXP
            self.generate_code(node.children[0])
            # AEXP_1
            resp = self.generate_code(node.children[1])
            if resp:
                operator = node.children[1].children[0].value
                self.code.append(f"lw $t0 4($sp)")
                self.pop_stack()
                if operator == "+":
                    self.code.append(f"add $a0, $t0, $a0")
                elif operator == "-":
                    self.code.append(f"sub $a0, $t0, $a0")
            else:
                return True

        elif node.value == "AEXP_1":
            if len(node.children) == 0:
                return
            self.push_stack(None)
            #MEXP
            self.generate_code(node.children[1])
            #AEXP_1
            resp = self.generate_code(node.children[2])
            if resp:
                operator = node.children[2].children[0].value
                self.code.append(f"lw $t0 4($sp)")
                self.pop_stack()
                if operator == "+":
                    self.code.append(f"add $a0, $t0, $a0")
                elif operator == "-":
                    self.code.append(f"sub $a0, $t0, $a0")
            else:
                return True
                    
        
        # TODO : ajeitar mult do num_aux = num * 3
        elif node.value == "MEXP":
            # SEXP
            self.generate_code(node.children[0])
            # MEXP_1
            resp = self.generate_code(node.children[1])
            if resp:
                self.code.append(f"lw $t0 4($sp)")
                self.pop_stack()
                self.code.append(f"mul $a0, $t0, $a0")
            else:
                return

        elif node.value == "MEXP_1":
            if len(node.children) == 0:
                return
            self.push_stack(None)
            #SEXP
            self.generate_code(node.children[1])
            # MEXP_1
            resp = self.generate_code(node.children[2])
            if resp:
                self.code.append(f"lw $t0 4($sp)")
                self.pop_stack()
                self.code.append(f"mul $a0, $t0, $a0")
            else:
                return True
                
        elif node.value == "SEXP":
            if node.children[0].kind == "NUMBER":
                self.code.append(f"li $a0, {node.children[0].value}")
            elif node.children[0].value == "!":
                self.generate_code(node.children[1])
                self.code.append("sltiu $a0, $a0 1")
            elif node.children[0].value == "-":
                self.generate_code(node.children[1])
                self.code.append("sub $a0, $zero, $a0")
            elif node.children[0].value == "true":
                self.code.append(f"li $a0, 1")
            elif node.children[0].value == "false":
                self.code.append(f"li $a0, 0")
                return reg
            elif node.children[0].value == "null":
                self.code.append(f"li $a0, 0")
                return reg
            # elif node.children[0].value == "new":
            # ! TODO
            #     node_parent = node.parent
            #     while node_parent != "CMD":
            #         node_parent = node.parent
            #     var_name = node_parent.children[0].value
            #     exp_value = node.children[3].children[0].value
            #     var_pos_stack = self.stack.index(var_name)
            #     for _ in range(exp_value):
            #         self.push_stack(var_name)
            #     self.stack.insert(var_pos_stack, var_name)
            #     self.generate_code(node.children[3])
            #     self.code.append("mult $a0, 4")
            #     self.code.append("sub $sp, $sp, $a0")
            elif node.children[0].value == "PEXP":
                self.generate_code(node.children[0])
                self.push_stack(None)
                self.generate_code(node.children[1])
                # self.code.append(f"lw $t0 4($sp)")
                # self.pop_stack()
                # self.code.append(f"add $a0, $a0, $t0")
                                
        elif node.value == "PEXP":
            if len(node.children) == 2:
                if node.children[0].kind == "IDENTIFIER":
                    resp = self.generate_code(node.children[1])
                    if not resp:
                        node_aux = node
                        while node_aux.value != "METODO":
                            node_aux = node_aux.parent
                        method_name = node_aux.children[2].value
                        var_name = node.children[0].value
                        if var_name in self.method_map[method_name]:
                            offset = (self.method_map[method_name].index(var_name) + 1) * 4
                            self.code.append(f"lw $a0, {offset}($fp)")
                        else:
                            offset = (self.stack.index(var_name) + 1) * 4
                            self.code.append(f"lw $a0, {offset}($sp)")
            elif len(node.children) == 4:
                self.generate_code(node.children[1])
                self.generate_code(node.children[3])
            elif len(node.children) == 5:
                self.generate_code(node.children[4])
                
        elif node.value == "PEXP_1":
            if len(node.children) == 3:
                method_name = node.children[1].value
                self.code.append(f"sw $fp 0($sp)")
                self.push_stack(None)
                self.code.append(f"addiu $sp, $sp, -4")
                self.generate_code(node.children[2])
                self.code.append(f"jal {method_name}")

        elif node.value == "PEXP_2":
            if len(node.children) == 4:
                self.generate_code(node.children[1])
                self.generate_code(node.children[3])
            elif len(node.children) == 2:
                self.generate_code(node.children[0])

        elif node.value == "EXPS":
            for child in node.children:
                self.generate_code(child)

        elif node.value == "EXPS_LIST":
            self.code.append("sw $a0 0($sp)")
            self.code.append("addiu $sp, $sp, -4")
            self.push_stack(None)
            if len(node.children) == 3:
                self.generate_code(node.children[1])
                self.generate_code(node.children[2])
            

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

    # code = """
    # class Factorial{ 
    #     public static void main(String[] a){ 
    #         System.out.println(new Fac().ComputeFac(20));
    #     } 
    # }
    # class Fac { 
    #     public int ComputeFac(int num, int[] a){
    #         int num_aux;
    #         if (num < 1)
    #             num_aux = 1;
    #         else
    #             num_aux = num * (this.ComputeFac(num-1, num));
    #         return num_aux ;
    #     } 
    # }
    # """

    # code = """
    # class Factorial{ 
    #     public static void main(String[] a){ 
    #         System.out.println(new Fac().ComputeFac(20, 10));
    #     } 
    # }
    # class Fac { 
    #     public int ComputeFac(int num, int num2){
    #         int num_aux;
    #         if (num < 1)
    #             num_aux = 1;
    #         else
    #             num_aux = num * (5 + 5);
    #         return num_aux ;
    #     } 
    # }
    # """

    code = """
    class Factorial{ 
        public static void main(String[] a){ 
            System.out.println(new Fac().ComputeFac(10));
        } 
    }
    class Fac { 
        public int ComputeFac(int num){
            int num_aux;
            num_aux = num * 3;
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

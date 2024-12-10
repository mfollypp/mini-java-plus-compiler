import re

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
        line_num = 1
        line_start = 0

        for match in self.regex.finditer(code):
            kind = match.lastgroup # Grupo foi informado no grupo de captura
            value = match.group(kind)
            column = match.start() - line_start
            
            if kind == 'WHITESPACE':
                if '\n' in value:
                    line_num += value.count('\n')
                    line_start = match.end()
                continue

            elif kind == 'COMMENT':
                if '\n' in value:
                    line_num += value.count('\n')
                    line_start = match.end()
                continue

            elif kind == 'NUMBER':
                value = int(value)  # Convert number to an integer

            tokens.append((kind, value, line_num, column))

        return tokens

# Example usage
if __name__ == "__main__":
    code = """
    class Example {
        public static void main(String[] args) {
            System.out.println(42);
        }
    }
    """

    scanner = Scanner()
    tokens = scanner.scan(code)
    for token in tokens:
        print(token)
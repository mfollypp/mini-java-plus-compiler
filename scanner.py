import re

class Token:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value
        
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

        for match in self.regex.finditer(code):
            kind = match.lastgroup # Grupo foi informado no grupo de captura
            value = match.group(kind)
            
            if kind in ['WHITESPACE', 'COMMENT']:
                continue

            elif kind == 'NUMBER':
                value = int(value)  # Convert number to an integer

            token = Token(kind, value)
            tokens.append(token)

        return tokens

# Example usage
if __name__ == "__main__":
    code = """
    class Factorial{
        public static void main(String[] a){
            System.out.println(new Fac().ComputeFac(10));
        }
    }
    """

    scanner = Scanner()
    tokens = scanner.scan(code)
    for token in tokens:
        print(token)
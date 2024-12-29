import re
class Token:
    def __init__(self,token_type,value):
        self.type = token_type
        self.value = value
    def __str__(self):
        return f"{self.type} : {self.value}"
        
class Lexer:
    def __init__(self,text):    
        self.text = text
        self.token_types = {'KEYWORD': r'\b(if|elif|else|for|while|return)\b' ,
                            'BOOL': r'\b(True|False)\b' ,
                            'STR': r'"[^"]*"' ,
                            'IDENTIFIER': r'[a-zA-Z_]\w*' ,
                            'FLOAT': r'\b-?\d+\.\d+\b' ,
                            'INT': r'\b-?\d+\b' ,
                            'OPERATOR': r'[+\-*/%]' ,
                            'COMMENT': r'#.*' ,
                            'WHITESPACE': r'\s+',
                            'MISMATCH': r'.'
                            }
        self.token_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in self.token_types.items())
        self.tokens = []
    
    def generateTokens(self):
        matches = re.finditer(self.token_regex,self.text)

        for match in matches:
            self.tokens.append(Token(match.lastgroup,match.group()))

        return self.tokens

def run(text):
    lexer = Lexer(text)
    tokens = lexer.generateTokens()
    return tokens 
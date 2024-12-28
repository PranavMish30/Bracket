import re
class Token:
    def __init__(self,token_type,value):
        self.type = token_type
        self.value = value
        
class Lexer:
    def __init__(self,text):    
        self.text = text
        self.token_types = {'KEYWORD': r'\b(if|elif|else|for|while|return)\b' ,
                            'IDENTIFIER': r'[a-zA-Z]\w*' ,
                            'INT': r'\b-?\d+\b' ,
                            'FLOAT': r'\b-?\d+\.\d+\b' ,
                            'STR': r'"[^"]*"' ,
                            'BOOL': r'\b(True|False)\b' ,
                            'OPERATOR': r'[+\-*/%]' ,
                            'COMMENT': r'//.*' ,
                            'WHITESPACE': r'\s+'
                            }
        self.tokens = []
    
    def generateTokens(self):
        for type,pattern in self.token_types.items():
            regex = re.compile(pattern)
            matches = regex.finditer(self.text)
            for match in matches:
                self.tokens.append(Token(type,match.group()))
        return self.tokens

def run(text):
    lexer = Lexer(text)
    tokens = lexer.generateTokens()
    return tokens 
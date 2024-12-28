import re
class Token:
    def __init__(self,value,token_type):
        self.type = token_type
        self.value = value
        
class Lexer:
    def __init__(self,text):    
        self.text = text
        self.token_types = {'KEYWORD': r'\b(if|elif|else|for|while|return)\b' ,
                            'IDENTIFIER': r'^[a-zA-Z]\w*' ,
                            'INT': r'\b-?\d+\b' ,
                            'FLOAT': r'\b-?\d+\.\d+\b' ,
                            'STR': r'\b"[^"]*"\b' ,
                            'BOOL': r'\b(True|False)\b' ,
                            'OPERATOR': r'\b[+\-*/%]\b' ,
                            'COMMENT': r'\b//.*' ,
                            'WHITESPACE': r'\s+'
                            }
        self.tokens = []
    
    def generateTokens(self):
        return self.tokens

def run(text):
    lexer = Lexer(text)
    tokens = lexer.generateTokens()
    return tokens 
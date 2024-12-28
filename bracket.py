class Token:
    def __init__(self,value,token_type):
        self.type = token_type
        self.value = value
        
class Lexer:
    def __init__(self,text):    
        self.text = text
        self.token_types = {}
        self.tokens = []
    
    def makeTokens(self):
        return self.tokens

def run(text):
    lexer = Lexer(text)
    tokens = lexer.makeTokens()
    return tokens 
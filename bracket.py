class Token:
    def __init__(self,value,t_type):
        self.type = t_type
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
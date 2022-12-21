
class TokenTypes:
    Int = "Int"
    Float = "Float"
    WhiteSpace = "WhiteSpace"
    Plus = "Plus"
    Minus = "Minus"
    Asterisk = "Asterisk"
    Slash = "Slash"
    LParenthesis = "LParenthesis"
    RParenthesis = "RParenthesis"
    BadToken = "BadToken"

class Token:
    def __init__(self, position, type_, text, value=None):
        self.position = position
        self.type = type_
        self.text = text
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.currentChar = self.text[self.position]

    def nextChar(self):
        self.position += 1
        self.currentChar = self.text[self.position] if self.position < len(self.text) else None

    def getTokens(self):
        tokens = []

        while self.currentChar != None:
            if self.currentChar==" ":
                start = self.position
                while self.currentChar==" ":
                    self.nextChar()

                length = self.position - start
                text = self.text[start:start+length]
                tokens.append(Token(start, TokenTypes.WhiteSpace, text))

            elif self.currentChar.isdigit():
                start = self.position
                while self.currentChar.isdigit() or self.currentChar==".":
                    self.nextChar()

                length = self.position - start
                text = self.text[start:start+length]

                value = float(text) if "." in text else int(text)
                type_ = TokenTypes.Float if "." in text else TokenTypes.Int
                tokens.append(Token(start, type_, text, value))

            elif self.currentChar == "+":
                tokens.append(Token(self.position, TokenTypes.Plus, "+"))
                self.nextChar()
            elif self.currentChar == "-":
                tokens.append(Token(self.position, TokenTypes.Minus, "-"))
                self.nextChar()
            elif self.currentChar == "*":
                tokens.append(Token(self.position, TokenTypes.Asterisk, "*"))
                self.nextChar()
            elif self.currentChar == "/":
                tokens.append(Token(self.position, TokenTypes.Slash, "/"))
                self.nextChar()
            elif self.currentChar == "(":
                tokens.append(Token(self.position, TokenTypes.LParenthesis, "("))
                self.nextChar()
            elif self.currentChar == ")":
                tokens.append(Token(self.position, TokenTypes.RParenthesis, ")"))
                self.nextChar()
            else:
                tokens.append(Token(self.position, TokenTypes.BadToken, ""))
                self.nextChar()

        return tokens


with open("C:/Users/ndmch/Documents/Projects/Slow/stages/lexer/test.sl", "r") as file:
    fileLines = file.read().splitlines()

    for line in fileLines:
        lexer = Lexer(line)
        tokens = lexer.getTokens()
        for token in tokens:
            print(token.__dict__)

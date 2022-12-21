
class SyntaxKind:
    NumberToken = "NumberToken"
    WhiteSpaceToken = "WhiteSpaceToken"
    PlusToken = "PlusToken"
    MinusToken = "MinusToken"
    StarToken = "StarToken"
    SlashToken = "SlashToken"
    OpenParenthesisToken = "OpenParenthesisToken"
    ClosedParenthesisToken = "ClosedParenthesisToken"
    BadToken = "BadToken"
    EndOfFileToken = "EndOfFileToken"
    BinaryExpression = "BinaryExpression"
    NumberExpressionSyntax = "NumberExpressionSyntax"

class SyntaxToken:
    def __init__(self, kind:SyntaxKind, position:int, text:str, value):
        self.kind = kind
        self.position = position
        self.text = text
        self.value = value

class Lexer:
    def __init__(self, text):
        self.text: str = text
        self.__position: int = 0

    def NextToken(self) -> SyntaxToken:
        """Detects <number>, <symbols> and <whitespaces>"""

        if self.__position >= len(self.text):
            return SyntaxToken(SyntaxKind.EndOfFileToken, self.__position, "\0", None)

        if self.text[self.__position].isdigit():
            start = self.__position
            while self.text[self.__position].isdigit():
                self.__position+=1

            length = self.__position - start
            text = self.text[start:start+length]
            value = int(text)
            return SyntaxToken(SyntaxKind.NumberToken, start, text, value)

        if self.text[self.__position]==" ":
            start = self.__position
            while self.text[self.__position]==" ":
                self.__position+=1

            length = self.__position - start
            text = self.text[start:start+length]
            return SyntaxToken(SyntaxKind.WhiteSpaceToken, start, text, None)

        start = self.__position
        self.__position+=1

        if self.text[start]=="+":
            return SyntaxToken(SyntaxKind.PlusToken, start, "+", None)
        elif self.text[start]=="-":
            return SyntaxToken(SyntaxKind.MinusToken, start, "-", None)
        elif self.text[start]=="*":
            return SyntaxToken(SyntaxKind.StarToken, start, "*", None)
        elif self.text[start]=="/":
            return SyntaxToken(SyntaxKind.SlashToken, start, "/", None)
        elif self.text[start]=="(":
            return SyntaxToken(SyntaxKind.OpenParenthesisToken, start, "(", None)
        elif self.text[start]==")":
            return SyntaxToken(SyntaxKind.ClosedParenthesisToken, start, ")", None)

        return SyntaxToken(SyntaxKind.BadToken, start, self.text[start:self.__position], None)


with open("C:/Users/ndmch/Documents/Projects/Slow/stages/lexer/test.sl", "r") as file:
    fileLines = file.read().splitlines()

    for line in fileLines:
        print(line)
        lexer = Lexer(line)
        token = lexer.NextToken()
        print(f"Kind: {token.kind}, Position: {token.position}, Text: {token.text}")

        while token.kind != SyntaxKind.EndOfFileToken:
            token = lexer.NextToken()
            print(f"Kind: {token.kind}, Position: {token.position}, Text: {token.text}")

        print("\n")

import lox
from lox_token import Token
from token_type import TokenType

class Scanner:
    
    keywords = {
        "and": TokenType.AND,
        "class": TokenType.CLASS,
        "else": TokenType.ELSE,
        "false": TokenType.FALSE,
        "for": TokenType.FOR,
        "if": TokenType.IF,
        "nil": TokenType.NIL,
        "or": TokenType.OR,
        "print": TokenType.PRINT,
        "return": TokenType.RETURN,
        "super": TokenType.SUPER,
        "this": TokenType.THIS,
        "true": TokenType.TRUE,
        "var": TokenType.VAR,
        "while": TokenType.WHILE
    }

    def __init__(self, source: str) -> None:
        self.source = source
        self.tokens = []
        self.start = 0
        self.current = 0
        self.line = 1


    def scan_tokens(self) -> list[Token]:
        while not self._is_at_end():
            self.start = self.current
            self.scan_token()
        
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens


    def _is_at_end(self) -> bool:
        return self.current >= len(self.source)


    def scan_token(self) -> None:
        c = self.advance()
        match c:
            # single char lexemes
            case '(':
                self.add_token_none(TokenType.LEFT_PAREN)
            case ')':
                self.add_token_none(TokenType.RIGHT_PAREN)
            case '{':
                self.add_token_none(TokenType.LEFT_BRACE)
            case '}':
                self.add_token_none(TokenType.RIGHT_BRACE)
            case ',':
                self.add_token_none(TokenType.COMMA)
            case '.':
                self.add_token_none(TokenType.DOT)
            case '-':
                self.add_token_none(TokenType.MINUS)
            case '+':
                self.add_token_none(TokenType.PLUS)
            case ';':
                self.add_token_none(TokenType.SEMICOLON)
            case '*':
                self.add_token_none(TokenType.STAR)
            
            # operators
            case '!':
                self.add_token_none(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=':
                self.add_token_none(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                self.add_token_none(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>':
                self.add_token_none(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            case '/':
                if self.match('/'):
                    while self.peek() != '\n' and not self._is_at_end():
                        self.advance()
                else:
                    self.add_token_none(TokenType.SLASH)

            # whitespace
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                self.line += 1
            
            # string literals
            case '"':
                self.string()

            case '_':
                if self.is_digit(c):
                    self.number()
                elif self.is_alpha(c):
                    self.identifier() 
                else:
                    lox.Lox.error(line, "Unexpected character.")


    def identifier(self) -> None:
        while self.is_alpha_numeric(self.peek()):
            self.advance()
        
        text = self.source[self.start, self.current]
        token_type = Scanner.keywords.get(text)
        if token_type is None:
            token_type = TokenType.IDENTIFIER 
        self.add_token_none(token_type)


    def match(self, expected: str) -> bool:
        if self._is_at_end():
            return False
        if self.source[self.current] != expected:
            return False
        self.current += 1
        return True
    

    def peek(self) -> bool:
        if self._is_at_end():
            return '\0'
        return self.source[self.current]


    def peek_next(self) -> str:
        if self.current + 1 >= len(self.source):
            return '/0'
        return self.source[self.current + 1]


    def number(self) -> None:
        while self.is_digit(self.peek()):
            self.advance()
        
        # look for fractional part
        if self.peek() == '.' and self.is_digit(self.peek_next()):
            self.advance()
        
        while self.is_digit(self.peek()):
            self.advance()
        
        self.add_token(TokenType.NUMBER, float(self.source[self.start, self.current]))
    

    def is_digit(self, c: str) -> bool:
        return c >= '0' and c <= '9'
    

    def is_alpha(self, c: str) -> bool:
        return c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c == '_'
    

    def is_alpha_numeric(self, c: str) -> bool:
        return self.is_alpha(c) or self.is_digit(c)
    

    def advance(self) -> str:
        char = self.source[self.current]
        self.current += 1
        return char
    

    def string(self) -> None:
        while self.peek() != '"' and not self._is_at_end():
            if self.peek() == '\n': 
                self.line += 1
            self.advance()
        
        if self._is_at_end():
            print(self.line, "Unterminated string.")
            return
        
        self.advance() # closing "

        value = self.source[self.start + 1, self.current - 1]
        self.add_token(TokenType.STRING, value)


    def add_token_none(self, token_type: TokenType) -> None:
        self.add_token(token_type, None)
    

    def add_token(self, token_type: TokenType, literal: object) -> None:
        text = self.source[self.start:self.current]
        self.tokens.append(Token(token_type, text, literal, self.line))



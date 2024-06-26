from expr import *
from token_type import *
from lox_token import Token

class AstPrinter(Visitor):
    def print(self, expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)
    
    def visit_grouping_expr(self, expr) -> str:
        return self.parenthesize("group", expr.expression)
    
    def visit_literal_expr(self, expr) -> str:
        if expr.value is None:
            return "nil"
        return str(expr.value)    
    
    def visit_unary_expr(self, expr) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)    

    def parenthesize(self, name: str, *exprs: Expr):
        return_str = "(" + name
        for expr in exprs:
            return_str += " "
            return_str += expr.accept(self)
        return_str += ")"
        return return_str

if __name__ == "__main__":
    expression = Binary(
        Unary(
            Token(TokenType.MINUS, "-", None, 1),
            Literal(123),
        ),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67))
    )
    printer = AstPrinter()

    print(printer.print(expression))
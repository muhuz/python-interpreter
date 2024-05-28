from expr import *
from token_type import *
from lox_token import Token

class AstPrinter(Expr):
    def __str__(self, expr):
        return expr.accept()

    def visit_binary_expr(expr) -> str:
        return parenthesize(expr.operator.lexeme, expr.left, expr.right)
    
    def visit_grouping_expr(expr) -> str:
        return parenthesize("group", expr.expression)
    
    def visit_literal_expr(expr) -> str:
        if expr.value is None:
            return "nil"
        return str(expr.value)    
    
    def visit_unary_expr(expr) -> str:
        return parenthesize(expr.operator.lexeme, expr.right)    

    def parenthesize(name: str, *exprs: Expr):
        return_str = "(" + name
        for expr in exprs:
            return_str += " "
            return_str += expr.accept()
        return_str += ")"
        return return_str

if __name__ == "__main__":
    expression = Binary(
        Token(TokenType.MINUS, "-", None, 1),
        Literal(123),
        Token(TokenType.STAR, "*", None, 1),
        Grouping(Literal(45.67))
    )
from abc import ABC, abstractmethod

from lox_token import Token

class Expr(ABC):
    pass

class Binary(Expr):
    def __init__(self, left: Expr, operator: Token, right: Expr) -> None:
        self.left = left
        self.operator = operator 
        self.right = right

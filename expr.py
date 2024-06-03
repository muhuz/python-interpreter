from abc import ABC, abstractmethod
from lox_token import Token

class Expr(ABC):
	pass

class Binary(Expr):
	def __init__(self, left: Expr, operator: Token, right: Expr):
		self.left = left
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitor.visit_binary_expr(self)

class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression = expression

	def accept(self, visitor):
		return visitor.visit_grouping_expr(self)

class Literal(Expr):
	def __init__(self, value: object):
		self.value = value

	def accept(self, visitor):
		return visitor.visit_literal_expr(self)

class Unary(Expr):
	def __init__(self, operator: Token, right: Expr):
		self.operator = operator
		self.right = right

	def accept(self, visitor):
		return visitor.visit_unary_expr(self)

class Visitor(ABC):
	def visit_binary_expr(expr: Binary):
		pass

	def visit_grouping_expr(expr: Grouping):
		pass

	def visit_literal_expr(expr: Literal):
		pass

	def visit_unary_expr(expr: Unary):
		pass



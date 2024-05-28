from abc import ABC, abstractmethodfrom lox_token import Token

class Expr(ABC):
	pass

class Visitor(ABC):
	def visitBinaryExpr(expr: Binary):
		pass

	def visitGroupingExpr(expr: Grouping):
		pass

	def visitLiteralExpr(expr: Literal):
		pass

	def visitUnaryExpr(expr: Unary):
		pass


class Binary(Expr):
	def __init__(self, left: Expr, operator: Token, right: Expr):
		self.left = left
		self.operator = operator
		self.right = right

class Grouping(Expr):
	def __init__(self, expression: Expr):
		self.expression = expression

class Literal(Expr):
	def __init__(self, value: Object):
		self.value = value

class Unary(Expr):
	def __init__(self, operator: Token, right: Expr):
		self.operator = operator
		self.right = right


	@abstractmethod
	def accept(visitor):
		return visitor.visitUnaryExpr()
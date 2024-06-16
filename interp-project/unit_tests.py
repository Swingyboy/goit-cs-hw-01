import unittest
from interpreter import Interpreter, Parser, Lexer


class TestInterpreter(unittest.TestCase):

    def test_addition(self):
        interpreter = Interpreter(Parser(Lexer("2 + 2")))
        self.assertEqual(interpreter.interpret(), 4)

    def test_subtraction(self):
        interpreter = Interpreter(Parser(Lexer("2 - 2")))
        self.assertEqual(interpreter.interpret(), 0)

    def test_multiplication(self):
        interpreter = Interpreter(Parser(Lexer("2 * 2")))
        self.assertEqual(interpreter.interpret(), 4)

    def test_division(self):
        interpreter = Interpreter(Parser(Lexer("2 / 2")))
        self.assertEqual(interpreter.interpret(), 1)

    def test_multiple_operations(self):
        interpreter = Interpreter(Parser(Lexer("2 + 2 * 2")))
        self.assertEqual(interpreter.interpret(), 6)

    def test_parentheses(self):
        interpreter = Interpreter(Parser(Lexer("(2 + 2) * 2")))
        self.assertEqual(interpreter.interpret(), 8)

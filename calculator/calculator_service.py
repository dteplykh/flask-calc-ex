from .exceptions import CalculatorZeroDevisionError


class CalculatorService:

    def calculate(self, operand_a: float, operand_b: float, operator: str) -> float:
        if operator == '*':
            return operand_a * operand_b
        elif operator == '/':
            try:
                return operand_a / operand_b
            except ZeroDivisionError:
                expression = f"{operand_a}{operator}{operand_b}"
                raise CalculatorZeroDevisionError(expression)
        elif operator == '+':
            return operand_a + operand_b
        elif operator == '-':
            return operand_a - operand_b

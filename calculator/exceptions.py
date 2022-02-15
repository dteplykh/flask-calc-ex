class CalculatorZeroDevisionError(Exception):
    def __init__(self, expression: str, message: str = "Devision by zerro error") -> None:
        super().__init__(message)
        self.message = message
        self.expression = expression

    def __str__(self) -> str:
        return f"Error in expression {self.expression}: {self.message} "

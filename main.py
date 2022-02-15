from calculator import CalculatorService
from web import WebApp


if __name__ == "__main__":
    calculator_service = CalculatorService()
    WebApp(
        calculator_service=calculator_service,
    ).run()

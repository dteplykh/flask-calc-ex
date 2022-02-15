import pytest
from web.web_app import WebApp
from calculator.calculator_service import CalculatorService


@pytest.fixture()
def web_app():
    web_app = WebApp(calculator_service=CalculatorService())
    web_app.app.config.update({
        "TESTING": True,
    })

    return web_app

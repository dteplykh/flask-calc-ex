
import pytest

from calculator import CalculatorService
from calculator.exceptions import CalculatorZeroDevisionError


@pytest.mark.parametrize(
    ("operand_a", "operator", "operand_b", "result"),
    (
        (1, "+", 2, 3),
        (3.5, "+", 2.4, 5.9),
        (1, "*", 2, 2),
        (3.6, "*", 2, 7.2),
        (1, "/", 2, 0.5),
        (3.6, "/", 2, 1.8),
        (1, "-", 2, -1),
        (3.5, "-", 2.4, 1.1),
    ))
def test_calculator_service_calculate(operand_a, operator, operand_b, result):
    calc = CalculatorService()
    # Act
    actual_result = calc.calculate(operand_a, operand_b, operator)
    # Assert
    assert actual_result == result


@pytest.mark.parametrize(
    ("operand_a", "operator", "operand_b", "exception"),
    (
        (1, "/", 0, CalculatorZeroDevisionError),
    ))
def test_calculator_service_calculate__exceptions(operand_a, operator, operand_b, exception):
    calc = CalculatorService()
    # Act & Assert
    with pytest.raises(exception) as ex_info:
        calc.calculate(operand_a, operand_b, operator)
    # Assert
    assert str(ex_info.value) == f"Error in expression {operand_a}{operator}{operand_b}: Devision by zerro error "
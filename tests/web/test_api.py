from http import HTTPStatus
from unittest.mock import patch
from calculator.calculator_service import CalculatorService
from calculator.exceptions import CalculatorZeroDevisionError


@patch.object(CalculatorService, 'calculate')
def test_calc_api(calculate_mock, web_app):
    client = web_app.app.test_client()
    calculate_mock.return_value = 3

    # Act
    response = client.post(
        '/calc/',
        data={'operand_a': "1", 'operand_b': "2", 'operator': '+'}
    )

    # Assert
    assert response.status_code == HTTPStatus.OK
    calculate_mock.assert_called_with(1.0, 2.0, '+')
    assert b'<input type="text" class="form-control" name="answer" id="answer" value="3" readonly="true">' in response.data


@patch.object(CalculatorService, 'calculate')
def test_calc_api_calculate_exception(calculate_mock, web_app):
    client = web_app.app.test_client()
    calculate_mock.side_effect = CalculatorZeroDevisionError("1.0/0.0")

    # Act
    response = client.post(
        '/calc/',
        data={'operand_a': "1", 'operand_b': "0", 'operator': '/'}
    )

    # Assert
    calculate_mock.assert_called_with(1.0, 0, '/')
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b'Error in expression 1.0/0.0: Devision by zerro error ' in response.data


@patch.object(CalculatorService, 'calculate')
def test_calc_api_invalid_params(calculate_mock, web_app):
    client = web_app.app.test_client()

    # Act
    response = client.post(
        '/calc/',
        data={'operand_a': "a", 'operand_b': "z", 'operator': '3'}
    )

    # Assert
    assert response.status_code == HTTPStatus.BAD_REQUEST
    assert b'{"operand_a":["Not a valid float value."],"operand_b":["Not a valid float value."],"operator":["Invalid value, must be one of: +, -, *, /."]}\n' in response.data

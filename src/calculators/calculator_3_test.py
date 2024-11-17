from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3.0

class MockDriverHandlerSuccess:
    def variance(self, numbers: List[float]) -> float:
        return 1000000.0

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as exception_info:
        calculator_3.calculate(mock_request)

    assert str(exception_info.value) == "Variance is less than multiplication"

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandlerSuccess())

    response = calculator_3.calculate(mock_request)
    assert response == {'data': {'calculator': 3, 'value': 1000000.0, 'success': True}}

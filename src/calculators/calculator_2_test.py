from typing import Dict, List
from .calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def standard_deviation(self, numbers: List[float]) -> float:
        return 3.0

# Teste unitário do Calculator2
def test_calculate_unit():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, Dict)
    assert formatted_response == {'data': {'calculator': 2, 'result': 0.33}}

# Teste de integração entre o Calculator2 e o NumpyHandler
def test_calculate_integration():
    mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
    
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    formatted_response = calculator_2.calculate(mock_request)

    assert isinstance(formatted_response, Dict)
    assert formatted_response == {'data': {'calculator': 2, 'result': 0.08}}

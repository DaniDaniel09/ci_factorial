import pytest
from src.factorial import factorial


def test_factorial_1():
    assert factorial(1) == 1


def test_factorial_no_enter():
    with pytest.raises(TypeError):
        factorial("hola")


def test_factorial_negativo():
    with pytest.raises(ValueError):
        factorial(-1)


def test_factorial_5():
    assert factorial(5) == 120

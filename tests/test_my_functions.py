import pytest
import source.my_functions as my_function


def test_add():
    result = my_function.add(1, 4)
    assert result == 5


def test_add_2():
    result = my_function.add(2, 4)
    assert result == 5

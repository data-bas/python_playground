import pytest
from source.shapes.shape import Shape
from source.shapes.square import Square


def test_square_is_subclass_of_shape():
    # Test of Square een subclass is van Shape
    assert issubclass(Square, Shape)


def test_square_implements_get_type():
    # Test of Square de get_type methode implementeert
    assert hasattr(Square, 'get_type')
    assert callable(Square.get_type)
    assert Square.get_type() == 'Square'


def test_square_implements_get_opp():
    # Test of Square de get_opp methode implementeert en correct werkt
    square = Square(2, 2)
    assert hasattr(square, 'get_opp')
    assert callable(square.get_opp)

    result = square.get_opp()

    # Controleer of het resultaat een float is
    assert isinstance(result, float)

    # Controleer of het resultaat de juiste waarde heeft
    assert result == 4.0  # Aangezien oppervlakte van een vierkant met zijden 2 en 2 gelijk is aan 4


def test_abstract_methods_in_shape():
    # Test of de abstracte methoden bestaan in Shape
    assert hasattr(Shape, 'get_opp')
    assert hasattr(Shape, 'get_type')
    with pytest.raises(TypeError):
        # Shape mag niet direct instantiëren omdat het abstract is
        shape = Shape()

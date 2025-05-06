import pytest
from source.dataclass.user import User


# from source.pydantic.user import User

def test_user_attributes():
    # Maak een User object
    user = User(username="john_doe", email="john@example.com", age=30)

    # Controleer of de attributen correct zijn ingesteld
    assert user.username == "john_doe"
    assert user.email == "john@example.com"
    assert user.age == 30
    assert user.active is True


def test_user_default_active():
    # Maak een User object zonder expliciet de active-parameter in te stellen
    user = User(username="jane_doe", email="jane@example.com", age=25)

    # Controleer of 'active' standaard True is
    assert user.active is True


def test_user_change_attributes():
    # Maak een User object
    user = User(username="john_doe", email="john@example.com", age=30)

    # Verander het attribuut 'active'
    user.active = False

    # Controleer of het attribuut correct is veranderd
    assert user.active is False

import pytest

from source.pydantic.user import User
from pydantic import ValidationError


def test_user_integration(postgres_db: object) -> None:
    """

    :rtype: object
    :param postgres_db:
    """
    # Arrange
    conn, cursor = postgres_db

    user = User(username="john_doe", email="john@example.com", age=30)
    user.save_to_db(cursor)
    conn.commit()
    # Act
    cursor.execute(f"SELECT username, email, age, active FROM users WHERE username = '{user.username}'")
    result = cursor.fetchone()

    # Assert
    assert result == (user.username, user.email, user.age, user.active)


def test_user_invalid_email(postgres_db):
    # Arrange
    conn, cursor = postgres_db

    # Act/Assert
    with pytest.raises(ValidationError):
        user = User(username="jane_doe", email="invalid-email", age=25)
        user.save_to_db(cursor)
        conn.commit()
        cursor.execute(f"SELECT username, email, age, active FROM users WHERE username = '{user.username}'")
        result = cursor.fetchone()


def test_user_invalid_age(postgres_db):
    # Arrange
    conn, cursor = postgres_db

    # Act/Assert
    with pytest.raises(ValidationError):
        user = User(username='henk', email='henk@hotmail.com', age=120)
        user.save_to_db(cursor)
        conn.commit()
        cursor.execute(f"SELECT username, email, age, active FROM users WHERE username = '{user.username}'")
        result = cursor.fetchone()

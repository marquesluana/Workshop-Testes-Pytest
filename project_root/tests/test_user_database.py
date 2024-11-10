import pytest
from user_database import UserDatabase

@pytest.fixture
def user_db():
    return UserDatabase()

def test_create_user(user_db):
    user_data = {"name": "Alice", "age": 1}
    user_id = "user1"
    created_user = user_db.create_user(user_id, user_data)

    assert created_user == user_data
    assert user_db.read_user(user_id) == user_data

def test_create_user_existing(user_db):
    user_id = "user1"
    user_data = {"name": "Alice", "age": 1}
    user_db.create_user(user_id, user_data)

    with pytest.raises(ValueError) as excinfo:
        user_db.create_user(user_id, user_data)

    assert "Usuário já existe." in str(excinfo.value)

def test_read_user(user_db):
    user_id = "user1"
    user_data = {"name": "Alice", "age": 1}
    user_db.create_user(user_id, user_data)

    assert user_db.read_user(user_id) == user_data
    assert user_db.read_user("nonexistent") is None

def test_update_user(user_db):
    user_id = "user1"
    user_data = {"name": "Alice", "age": 1}
    user_db.create_user(user_id, user_data)

    new_data = {"age": 2}
    updated_user = user_db.update_user(user_id, new_data)

    assert updated_user["age"] == 2
    assert updated_user["name"] == "Alice"

def test_update_user_nonexistent(user_db):
    with pytest.raises(ValueError) as excinfo:
        user_db.update_user("nonexistent", {"age": 40})

    assert "Usuário não existe." in str(excinfo.value)

def test_delete_user(user_db):
    user_id = "user1"
    user_data = {"name": "Alice", "age": 1}
    user_db.create_user(user_id, user_data)

    assert user_db.delete_user(user_id) is True
    assert user_db.read_user(user_id) is None

def test_delete_user_nonexistent(user_db):
    with pytest.raises(ValueError) as excinfo:
        user_db.delete_user("nonexistent")

    assert "Usuário não existe." in str(excinfo.value)

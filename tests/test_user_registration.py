def test_user_registration():
    user_data = {
        "email": "testuser@mail.com",
        "password": "testpassword",
    }
    result = register_user(user_data)
    assert result is not None
    assert result["email"] == user_data["email"]

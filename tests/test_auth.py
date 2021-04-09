from new_feature import auth


def test_login():
    assert auth.login() is True

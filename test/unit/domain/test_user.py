from src.domain.user import User


def test__create_user__with_valid_values__user_created():
    user = User(
        user_id=1,
        email="someone@gmail.com",
        fullname="someone"
    )

    assert user.user_id == 1
    assert user.email == "someone@gmail.com"
    assert user.fullname == "someone"

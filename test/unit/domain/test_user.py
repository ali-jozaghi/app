from src.domain.user import User
from src.common.result import Status


def test__create_user__with_valid_values__user_created():
    create_user = User.create(
        user_id=1,
        email="someone@gmail.com",
        fullname="someone"
    )
    assert create_user.status == Status.SUCCESS
    assert create_user.data.user_id == 1
    assert create_user.data.email == "someone@gmail.com"
    assert create_user.data.fullname == "someone"


def test__create_user__with_empty_email__return_failure():
    create_user = User.create(
        user_id=1,
        email="",
        fullname="someone"
    )
    assert create_user.status == Status.FAILURE
    assert create_user.error == "email is required."

from src.repository.user_repository import UserRepository
from ..test_startup import database_connection, database_info
from src.domain.user import User
from src.common.result import Status


def test_user_repository__save__pass_valid_user__user_inserted(database_connection):
    user_repository = UserRepository(database_connection)
    user = User(
        user_id=0,
        email="someone@gmail.com",
        fullname="someone"
    )
    save_user = user_repository.save(user)

    assert save_user.status == Status.SUCCESS
    user_id = save_user.data

    new_user = user_repository.get_by_id(user_id)
    assert new_user is not None
    assert new_user.email == user.email
    assert new_user.fullname == user.fullname








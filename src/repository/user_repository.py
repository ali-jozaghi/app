from sqlalchemy import insert, select

from src.domain.user import User
from src.common.result import Result
from src.repository.database import users


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def _insert(self, user: User) -> Result[int]:
        insert_command = insert(users).values(
            email=user.email,
            fullname=user.fullname
        )
        result = self._connection.execute(insert_command)
        return Result.success(result.inserted_primary_key[0])

    def _update(self, user: User) -> Result[int]:
        pass

    def save(self, user: User) -> Result[int]:
        if user.is_new():
            return self._insert(user)
        else:
            return self._update(user)

    def get_by_id(self, user_id: int) -> User:
        query = select([users]).where(users.c.user_id == user_id)
        result = self._connection.execute(query)
        result = result.first()
        if not result:
            return None
        return User(
            user_id=result.user_id,
            email=result.email,
            fullname=result.fullname
        )

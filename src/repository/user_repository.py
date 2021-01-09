from sqlalchemy import insert, select

from src.domain.user import User
from src.common.result import Result
from src.repository.database import users
from src.repository.base_repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

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

    def _get_user(self, query) -> User:
        result = self.select_one(users, query)
        if not result:
            return None
        return User(
            user_id=result.user_id,
            email=result.email,
            fullname=result.fullname
        )

    def get_by_id(self, user_id: int) -> User:
        return self._get_user(users.c.user_id == user_id)

    def get_by_email(self, email: str) -> User:
        return self._get_user(users.c.email == email)

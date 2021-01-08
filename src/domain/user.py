from dataclasses import dataclass
from src.common.result import Result
from src.common.validators import empty_or_none_string


@dataclass
class User:
    user_id: int
    email: str
    fullname: str

    def is_new(self) -> bool:
        return self.user_id == 0

    @classmethod
    def create(cls, email: str, fullname: str, user_id: int = 0):
        if empty_or_none_string(email):
            return Result.failure("email is required.")

        if empty_or_none_string(fullname):
            return Result.failure("fullname is required")

        user = cls(
            user_id=user_id,
            email=email,
            fullname=fullname
        )
        return Result.success(user)


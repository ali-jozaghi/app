from dataclasses import dataclass
from src.common.result import Result
from src.common.validators import is_empty_or_none_string


@dataclass
class User:
    user_id: int
    email: str
    fullname: str

    @classmethod
    def create(cls, **kwargs):
        if "email" not in kwargs or is_empty_or_none_string(kwargs["email"]):
            return Result.failure("email is required.")

        user = cls(**kwargs)
        return Result.success(user)


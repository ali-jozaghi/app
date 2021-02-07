from dataclasses import dataclass
from src.common.result import Result
from src.common.validators import empty_or_none_string, not_valid_email, not_int
from src.repository.user_repository import UserRepository
from src.domain.user import User


@dataclass
class CreateUserRequest:
    fullname: str
    email: str

    @classmethod
    def create(cls, fullname: str, email: str):
        if empty_or_none_string(fullname):
            return Result.failure("fullname is required.")
        if empty_or_none_string(email):
            return Result.failure("email is required.")
        if not_valid_email(email):
            return Result.failure("email is invalid.")

        request = cls(
            fullname=fullname,
            email=email
        )
        return Result.success(request)


@dataclass
class CreateUserResponse:
    user_id: int


class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    def execute(self, request: CreateUserRequest) -> Result[CreateUserResponse]:

        existing_user = self._user_repository.get_by_email(request.email)
        if existing_user:
            return Result.failure("user with the same email is already exists.")

        create_user = User.create(
            email=request.email,
            fullname=request.fullname
        )

        if create_user.is_failure():
            return Result.failure(create_user.error)

        user = create_user.data

        save_user = self._user_repository.save(user)

        if save_user.is_failure():
            return Result.failure(save_user.error)

        response = CreateUserResponse(
            user_id=save_user.data
        )

        return Result.success(response)



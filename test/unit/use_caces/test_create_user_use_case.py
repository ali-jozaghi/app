from unittest import mock
from src.common.result import Result
from src.use_caces.create_user_use_case import CreateUserUseCase, CreateUserRequest, CreateUserResponse


def test_execute__pass_valid_request__user_created():
    user_repository = mock.Mock()
    user_repository.get_by_email.return_value = None
    user_repository.save.return_value= Result.success(50)
    create_user_use_case = CreateUserUseCase(user_repository)

    request = CreateUserRequest.create("someone", "someone@gmail.com")

    response = create_user_use_case.execute(request.data)

    user_repository.get_by_email.assert_called_with("someone@gmail.com")
    user_repository.save.assert_called()

    assert response.is_success()
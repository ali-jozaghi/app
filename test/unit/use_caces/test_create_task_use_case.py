from unittest import mock
from src.use_caces.create_task_use_case import CreateTaskRequest, CreateTaskUseCase
from src.domain.user import User
from src.common.result import Status, Result
import pytest


@pytest.fixture
def valid_owner():
    return User.create(
        user_id=1234,
        email="someone@gmail.com",
        fullname="someone"
    )


# test CreateTaskRequest
def test__create_task_request__pass_valid_values__request_created():
    create_request = CreateTaskRequest.create(
        title="some task",
        owner_id=1234,
        details="some details about the task",
        story_points=5
    )

    assert create_request.status == Status.SUCCESS
    assert create_request.data.title == "some task"
    assert create_request.data.owner_id == 1234
    assert create_request.data.details == "some details about the task"
    assert create_request.data.story_points == 5


def test__create_task_request__pass_no_title__return_failure():
    create_request = CreateTaskRequest.create(
        owner_id=1234,
        details="some details about the task",
        story_points=5
    )

    assert create_request.status == Status.FAILURE
    assert create_request.error == "title is required."


def test__create_task_request__pass_empty_title__return_failure():
    create_request = CreateTaskRequest.create(
        title="",
        owner_id=1234,
        details="some details about the task",
        story_points=5
    )

    assert create_request.status == Status.FAILURE
    assert create_request.error == "title is required."


def test__create_task_request__pass_no_owner_id__return_failure():
    create_request = CreateTaskRequest.create(
        title="something",
        details="some details about the task",
        story_points=5
    )

    assert create_request.status == Status.FAILURE
    assert create_request.error == "owner_id is required."


# test CreateTaskUseCase
def test__create_task_use_case__passing_valid_values__task_created(valid_owner):
    user_repo = mock.Mock()
    user_repo.get_by_id.return_value = valid_owner

    task_repo = mock.Mock()
    task_repo.save.return_value = Result.success(4000)
    request = CreateTaskRequest(
        title="some task",
        owner_id=1234,
        details="some details about the task",
        story_points=5
    )
    use_case = CreateTaskUseCase(user_repo, task_repo)

    response = use_case.execute(request)

    user_repo.get_by_id.assert_called_with(1234)

    assert response.status == Status.SUCCESS
    assert response.data.task_id == 4000


def test__create_task_use_case__invalid_owner_id__returns_failure_result():
    user_repo = mock.Mock()
    user_repo.get_by_id.return_value = None
    task_repo = mock.Mock()
    request = CreateTaskRequest(
        title="some task",
        owner_id=0,
        details="some details about the task",
        story_points=5
    )
    use_case = CreateTaskUseCase(user_repo, task_repo)

    response = use_case.execute(request)

    assert response.status == Status.FAILURE
    assert response.error == "owner_id is not valid."

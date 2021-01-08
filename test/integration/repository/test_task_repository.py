import pytest
from ..test_startup import database_connection
from src.repository.task_repository import TaskRepository
from src.repository.user_repository import UserRepository
from src.domain.task import Task
from src.domain.user import User
from datetime import datetime
from src.common.result import Status


@pytest.fixture
def valid_user(database_connection):
    user_repository = UserRepository(database_connection)
    user = User.create("someone@mail.com", "someone")
    save_user_result = user_repository.save(user.data)
    saved_user = user_repository.get_by_id(save_user_result.data)
    return saved_user


def test_task_repository__save__pass_valid_task__task_is_save(database_connection, valid_user):
    task_repository = TaskRepository(database_connection)
    created_at = datetime.utcnow()
    create_task_result = Task.create(
        title="task one",
        details="some details about the task",
        owner=valid_user,
        created_at=created_at,
        story_points=5
    )
    task = create_task_result.data
    save_task_result = task_repository.save(task)

    assert save_task_result.status == Status.SUCCESS
    saved_task_id = save_task_result.data
    saved_task = task_repository.get_by_id(saved_task_id, eager_loading=True)

    assert saved_task is not None
    assert saved_task.task_id == saved_task_id
    assert saved_task.title == task.title
    assert saved_task.details == task.details
    assert saved_task.owner.user_id == task.owner.user_id
    assert saved_task.created_at == task.created_at
    assert saved_task.story_points == task.story_points


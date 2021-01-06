from src.domain.task import Task
from src.domain.user import User
from datetime import datetime
from src.common.result import Status


def test_create_task_with_valid_values():
    now = datetime.now()
    owner = User(
        user_id=123,
        email="someone@gamil.com",
        fullname="someone"
    )
    create_task = Task.create(
        title="task one",
        owner=owner,
        details="first task for the team",
        created_at=now,
        story_points=5
    )
    assert create_task.status == Status.SUCCESS
    task = create_task.data

    assert task.title == "task one"
    assert task.owner.user_id == 123
    assert task.owner.fullname == "someone"
    assert task.owner.email == "someone@gamil.com"
    assert task.details == "first task for the team"
    assert task.created_at == now
    assert task.story_points == 5
    assert task.task_id == 0

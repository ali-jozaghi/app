from src.repository.user_repository import UserRepository
from src.repository.task_repository import TaskRepository
from src.common.result import Result
from src.domain.task import Task
from datetime import datetime
from dataclasses import dataclass
from src.common.validators import empty_or_none_string, not_int


@dataclass
class CreateTaskRequest:
    title: str
    details: str
    story_points: int
    owner_id: int

    @classmethod
    def create(cls, title: str, details: str, story_points: int, owner_id: int):
        if empty_or_none_string(title):
            return Result.failure("title is required.")

        if not_int(owner_id):
            return Result.failure("owner_id is required.")

        if not_int(story_points):
            return Result.failure("story_points is required.")

        request = cls(
            title=title,
            details=details,
            story_points=story_points,
            owner_id=owner_id
        )
        return Result.success(request)


@dataclass
class CreateTaskResponse:
    task_id: int


class CreateTaskUseCase:
    def __init__(self, user_repository: UserRepository, task_repository: TaskRepository) -> None:
        self.user_repository = user_repository
        self.task_repository = task_repository

    def execute(self, request: CreateTaskRequest) -> Result[CreateTaskResponse]:
        owner = self.user_repository.get_by_id(request.owner_id)
        if not owner:
            return Result.failure("owner_id is not valid.")

        create_task = Task.create(
            title=request.title,
            owner=owner,
            details=request.details,
            created_at=datetime.utcnow(),
            story_points=request.story_points
        )
        if create_task.is_failure():
            return Result.failure(create_task.error)

        save_task = self.task_repository.save(create_task.data)

        if save_task.is_failure():
            return Result.failure(save_task.error)

        response = CreateTaskResponse(task_id=save_task.data)

        return Result.success(response)

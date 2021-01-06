from src.repository.user_repository import UserRepository
from src.repository.task_repository import TaskRepository
from src.common.result import Result
from src.domain.task import Task
from datetime import datetime
from dataclasses import dataclass


@dataclass
class CreateTaskRequest:
    title: str
    details: str
    story_points: str
    owner_id: int


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

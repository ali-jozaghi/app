from datetime import datetime
from src.domain.user import User
from src.common.result import Result
from dataclasses import dataclass

@dataclass
class Task:
    task_id: int
    title: str
    owner: User
    details: str
    created_at: datetime
    story_points: int

    @classmethod
    def create(cls, **kwargs):
        if "task_id" not in kwargs:
            kwargs["task_id"] = 0

        if kwargs["owner"] is None:
            return Result.failure("owner is required.")

        task = cls(**kwargs)
        return Result.success(task)



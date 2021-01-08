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

    def is_new(self):
        return self.task_id == 0

    @classmethod
    def create(cls,
               title: str,
               details: str,
               owner: User,
               story_points: int,
               task_id: int = 0,
               created_at: datetime = datetime.utcnow()):

        if owner is None:
            return Result.failure("owner is required.")

        task = cls(
            title=title,
            details=details,
            owner=owner,
            story_points=story_points,
            task_id=task_id,
            created_at=created_at
        )
        return Result.success(task)



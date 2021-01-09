from src.common.result import Result
from src.domain.task import Task
from src.domain.user import User
from src.repository.database import tasks, users
from sqlalchemy import insert, select
from src.repository.base_repository import BaseRepository


class TaskRepository(BaseRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def create(self, task: Task) -> Result[int]:
        insert_command = insert(tasks).values(
            title=task.title,
            details=task.details,
            story_points=task.story_points,
            owner_id=task.owner.user_id,
            created_at=task.created_at
        )
        result = self._connection.execute(insert_command)
        return Result.success(result.inserted_primary_key[0])

    def update(self, task: Task) -> Result[int]:
        raise NotImplementedError()

    def save(self, task: Task) -> Result[int]:
        if task.is_new():
            return self.create(task)
        else:
            return self.update(task)

    def get_by_id(self, task_id: int, eager_loading: bool = False) -> Task:
        query = select([tasks]).where(tasks.c.task_id == task_id)
        result = self._connection.execute(query)
        result = result.first()
        if not result:
            return None

        owner = None
        if eager_loading:
            get_owner_result = self.select_one(users, users.c.user_id == result.owner_id)
            if get_owner_result:
                owner = User(
                    user_id=get_owner_result.user_id,
                    email=get_owner_result.email,
                    fullname=get_owner_result.fullname
                )

        return Task(
            title=result.title,
            details=result.details,
            owner=owner,
            story_points=result.story_points,
            task_id=result.task_id,
            created_at=result.created_at
        )

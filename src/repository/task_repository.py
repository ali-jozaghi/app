from src.common.result import Result
from src.domain.task import Task
from src.repository.database import tasks
from sqlalchemy import insert, select
from src.repository.user_repository import UserRepository


class TaskRepository:
    def __init__(self, connection):
        self._connection = connection
        self._user_repository = UserRepository(connection)

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
        pass

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
            owner = self._user_repository.get_by_id(result.owner_id)

        return Task(
            title=result.title,
            details=result.details,
            owner=owner,
            story_points=result.story_points,
            task_id=result.task_id,
            created_at=result.created_at
        )

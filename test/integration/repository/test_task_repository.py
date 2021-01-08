from ..test_startup import database_connection
from src.repository.task_repository import TaskRepository

def test_task_repository__save__pass_valid_task__task_is_save(database_connection):
    task_repository = TaskRepository(database_connection)


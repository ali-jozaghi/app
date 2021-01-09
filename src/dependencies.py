from src.configuration import setting
from fastapi import Depends
from src.repository.database import Database
from src.repository.user_repository import UserRepository
from src.repository.task_repository import TaskRepository
from src.use_caces.create_task_use_case import CreateTaskUseCase
from src.use_caces.create_user_use_case import CreateUserUseCase
from src.repository.database import DatabaseInfo


def get_configuration():
    return setting


def get_connection(config=Depends(get_configuration)):
    database_info = DatabaseInfo(
        username=config.database_username,
        password=config.database_password,
        host=config.database_host,
        port=config.database_port,
        name=config.database_name
    )
    return Database(database_info).connect()


def get_user_repository(connection=Depends(get_connection)):
    return UserRepository(connection)


def get_task_repository(connection=Depends(get_connection)):
    return TaskRepository(connection)


def get_create_task_use_case(
        user_repository=Depends(get_user_repository),
        task_repository=Depends(get_task_repository)):
    return CreateTaskUseCase(user_repository, task_repository)


def get_create_user_use_case(user_repository=Depends(get_user_repository)):
    return CreateUserUseCase(user_repository)

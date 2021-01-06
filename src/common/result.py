from enum import Enum
from typing import TypeVar, Generic


class Status(str, Enum):
    SUCCESS = 'SUCCESS'
    FAILURE = 'FAILURE'


T = TypeVar('T')


class Result(Generic[T]):
    def __init__(self, status: Status, data: T = None, error: str = None):
        self.status = status
        self.data = data
        self.error = error

    def is_success(self):
        return self.status == Status.SUCCESS

    def is_failure(self):
        return not self.is_success()

    @classmethod
    def success(cls, data: T = None):
        return Result(
            status=Status.SUCCESS,
            data=data
        )

    @classmethod
    def failure(cls, error: str):
        return Result(
            status=Status.FAILURE,
            error=error
        )

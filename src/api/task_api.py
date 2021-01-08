from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_create_task_use_case
from src.use_caces.create_task_use_case import CreateTaskRequest, CreateTaskResponse

router = APIRouter(
    prefix='/tasks'
)


@router.post('/', response_model=CreateTaskResponse)
async def create_task(
        request: CreateTaskRequest,
        create_task_use_case=Depends(get_create_task_use_case)
):
    result = create_task_use_case.execute(request)
    if result.failure():
        raise HTTPException(400, result.error)

    return result.data


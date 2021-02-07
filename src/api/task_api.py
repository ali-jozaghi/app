from fastapi import APIRouter, Depends, HTTPException, Body
from src.dependencies import get_create_task_use_case
from src.use_caces.create_task_use_case import CreateTaskRequest, CreateTaskResponse

router = APIRouter(
    prefix='/tasks'
)


@router.post('/', response_model=CreateTaskResponse)
async def create_task(
        title: str = Body(...),
        details: str = Body(...),
        story_points: int = Body(...),
        owner_id: int = Body(...),
        create_task_use_case=Depends(get_create_task_use_case)
):
    create_request = CreateTaskRequest.create(title, details, story_points, owner_id)
    if create_request.is_failure():
        raise HTTPException(400, create_request.error)

    result = create_task_use_case.execute(create_request.data)
    if result.is_failure():
        raise HTTPException(400, result.error)

    return result.data


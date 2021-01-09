from fastapi import APIRouter, Depends, HTTPException
from src.dependencies import get_create_user_use_case
from src.use_caces.create_user_use_case import CreateUserRequest, CreateUserResponse

router = APIRouter(
    prefix='/users'
)


@router.post("", response_model=CreateUserResponse)
async def create_user(
        request: CreateUserRequest,
        create_user_use_case=Depends(get_create_user_use_case)
):
    result = create_user_use_case.execute(request)
    if result.is_failure():
        raise HTTPException(400, result.error)

    return result.data


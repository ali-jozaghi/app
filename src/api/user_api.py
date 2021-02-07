from fastapi import APIRouter, Depends, HTTPException, Body
from src.dependencies import get_create_user_use_case
from src.use_caces.create_user_use_case import CreateUserRequest, CreateUserResponse

router = APIRouter(
    prefix='/users'
)


@router.post("", response_model=CreateUserResponse)
async def create_user(
        fullname: str = Body(...),
        email: str = Body(...),
        create_user_use_case=Depends(get_create_user_use_case)
):
    create_request = CreateUserRequest.create(fullname, email)
    if create_request.is_failure():
        raise HTTPException(400, create_request.error)

    result = create_user_use_case.execute(create_request.data)
    if result.is_failure():
        raise HTTPException(400, result.error)

    return result.data


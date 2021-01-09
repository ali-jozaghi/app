from fastapi import FastAPI
from src.api import task_api
from src.api import user_api

app = FastAPI()

app.include_router(task_api.router)
app.include_router(user_api.router)

from fastapi import FastAPI
from src.api import task_api

app = FastAPI()

app.include_router(task_api.router)

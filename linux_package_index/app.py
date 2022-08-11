from fastapi import FastAPI
from linux_package_index.routes import index
from sqlmodel import SQLModel
from linux_package_index.db import engine

SQLModel.metadata.create_all(engine)

app = FastAPI()

app.include_router(index.router, prefix="/packages")

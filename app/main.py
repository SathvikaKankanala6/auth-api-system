from fastapi import FastAPI
from sqlmodel import SQLModel
from .db import engine
from .routes import auth, protected

app = FastAPI(title="Auth API System")

SQLModel.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(protected.router)

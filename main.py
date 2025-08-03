from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import Annotated

import models
from database import SessionLocal, engine
from models import Todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def read_all(db: Annotated[Session, Depends(get_db)]):
    return db.query(Todos).all()

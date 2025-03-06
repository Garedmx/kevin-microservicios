from fastapi import FastAPI
from .database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/db_service/")
def get_db_service():
    return {"message": "Welcome to the Data Manager microservice"}
from database.database import SessionLocal

from fastapi import FastAPI

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def index():
    return {
        "message": "Hello, I am a python app deployed by FluxCD ",
    }

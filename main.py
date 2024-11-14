from fastapi import FastAPI, Depends, HTTPException
from connection import get_db
from models.authors import get_authors
# from sqlalchemy.orm import Session

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/authors")
# def all_authors(db: Session = Depends(get_db)):
#     authors = get_authors(db)
#     if authors is None:
#         raise HTTPException(status_code=400, detail="No Authors Found")
#     return authors
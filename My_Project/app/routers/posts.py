
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

router = APIRouter(
    prefix="/posts",
    tags=["posts"]
)


@router.post("/", response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)


@router.get("/{post_id}", response_model=schemas.Post)
def read_posts(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.get("/", response_model=schemas.Post)
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db=db)


@router.put("/{post_id}", response_model=schemas.Post)
def update_posts(post_id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_post = crud.update_post(db=db, post_id=post_id, post_update=post)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post


@router.delete("/{post_id}", response_model=schemas.Post)
def delete_posts(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.delete_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not delete")
    return db_post

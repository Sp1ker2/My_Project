from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
import app.schemas as schemas
import app.crud as crud

router = APIRouter(
    prefix="/tags",
    tags=["tags"]
)



@router.get("/", response_model=List[schemas.Tag])
def read_tags(db: Session = Depends(get_db)):
    return crud.get_tags(db=db)

@router.get("/{tag_id}", response_model=schemas.Tag)
def read_tags(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.get_tag(db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag
@router.post("/", response_model=schemas.Tag)
def create_tag(tag: schemas.TagCreate, db: Session = Depends(get_db)):
    return crud.create_tag(db=db, tag=tag)
@router.put("/{tag_id}", response_model=schemas.Tag)
def update_tags(tag_id: int, tag: schemas.TagCreate, db: Session = Depends(get_db)):
    db_tag = crud.update_tag(db=db, tag_id=tag_id, tag_update=tag)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@router.delete("/{tag_id}", response_model=schemas.Tag)
def delete_tags(tag_id: int, db: Session = Depends(get_db)):
    db_tag = crud.delete_tag(db=db, tag_id=tag_id)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

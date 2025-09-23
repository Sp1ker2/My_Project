from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from crm_app import models, schemas, database, crud
from crm_app.auth import get_current_user

router = APIRouter(prefix="/clients", tags=["clients"])

# ------------------------------
# Получить всех клиентов с фильтрацией по роли
# ------------------------------
@router.get("/", response_model=List[schemas.ClientOut])
def read_clients(
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    if current_user.role == "ADMIN":
        return db.query(models.Client).all()
    elif current_user.role == "TEAM":
        return db.query(models.Client).filter(models.Client.team_id == current_user.team_id).all()
    else:  # CALL
        return db.query(models.Client).filter(models.Client.user_id == current_user.id).all()


# ------------------------------
# Создать клиента
# ------------------------------
@router.post("/", response_model=schemas.ClientOut)
def create_client(
    client: schemas.ClientCreate,
    team_id: int,  # сюда передаем ID тимлидера
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    if current_user.role != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    db_client = models.Client(
        name=client.name,
        email=client.email,
        phone=client.phone,
        status=client.status,
        team_id=team_id,  # назначаем Team-лидеру
        user_id=None  # пока никто не назначен
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client



# ------------------------------
# Назначить клиента на Call
# ------------------------------
@router.post("/assign_to_call/{client_id}/{call_id}", response_model=schemas.ClientOut)
def assign_client_to_call(
    client_id: int,
    call_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    if current_user.role != "TEAM":
        raise HTTPException(status_code=403, detail="Not enough permissions")

    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    if client.team_id != current_user.team_id:
        raise HTTPException(status_code=403, detail="Client is not in your team")

    call_user = db.query(models.User).filter(models.User.id == call_id, models.User.role == "CALL").first()
    if not call_user:
        raise HTTPException(status_code=404, detail="Call user not found")

    client.user_id = call_user.id
    db.commit()
    db.refresh(client)
    return client


# ------------------------------
# Получить клиента по ID
# ------------------------------
@router.get("/{client_id}", response_model=schemas.ClientOut)
def read_client(
    client_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    if current_user.role == "TEAM" and client.team_id != current_user.team_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    if current_user.role == "CALL" and client.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    return client

@router.post("/{client_id}/assign_call/{call_id}", response_model=schemas.ClientOut)
def assign_client_to_call(
    client_id: int,
    call_id: int,
    current_user: models.User = Depends(get_current_user),
    db: Session = Depends(database.get_db)
):
    if current_user.role != models.UserRole.TEAM:
        raise HTTPException(status_code=403, detail="Not enough permissions")

    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")

    if client.team_id != current_user.team_id:
        raise HTTPException(status_code=403, detail="Cannot assign client from another team")

    call_user = db.query(models.User).filter(models.User.id == call_id, models.User.role == models.UserRole.CALL).first()
    if not call_user:
        raise HTTPException(status_code=404, detail="Call not found")

    client.user_id = call_id
    db.commit()
    db.refresh(client)
    return client
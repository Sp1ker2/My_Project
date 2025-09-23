from sqlalchemy.orm import Session
from crm_app import models, schemas
from crm_app.models import User, UserRole, Client
from fastapi import Depends, HTTPException
from crm_app.database import get_db
def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def create_client(db: Session, client: schemas.ClientCreate):
    tags = []
    for tag in getattr(client, "tags", []):
        db_tag = db.query(models.Tag).filter(models.Tag.name == tag.name).first()
        if not db_tag:
            db_tag = models.Tag(name=tag.name)
            db.add(db_tag)
            db.commit()
            db.refresh(db_tag)
        tags.append(db_tag)

    db_client = models.Client(
        name=client.name,
        email=client.email,
        phone=client.phone,
        status=client.status,
        tags=tags
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db: Session, client_id: int, client: schemas.ClientBase):
    db_client = get_client(db, client_id)
    if db_client:
        db_client.name = client.name
        db_client.email = client.email
        db_client.phone = client.phone
        db_client.status = client.status

        # Обновляем теги
        if hasattr(client, "tags"):
            tags = []
            for tag in client.tags:
                db_tag = db.query(models.Tag).filter(models.Tag.name == tag.name).first()
                if not db_tag:
                    db_tag = models.Tag(name=tag.name)
                    db.add(db_tag)
                    db.commit()
                    db.refresh(db_tag)
                tags.append(db_tag)
            db_client.tags = tags

        db.commit()
        db.refresh(db_client)
    return db_client

def delete_client(db: Session, client_id: int):
    db_client = get_client(db, client_id)
    if db_client:
        db.delete(db_client)
        db.commit()
    return db_client

def get_clients_by_multiple_tags(db: Session, tag_names: list[str]):
    return db.query(models.Client)\
             .join(models.Client.tags)\
             .filter(models.Tag.name.in_(tag_names))\
             .order_by(models.Client.status)\
             .all()




def create_team(db: Session, team: schemas.TeamBase):
    db_team = models.Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        password=user.password,  # В продакшене хэшировать!
        role=user.role,
        team_id=user.team_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_calls_for_user(db: Session, current_user: User):
    if current_user.role == UserRole.ADMIN:
        return db.query(Client).join(User).filter(User.role == UserRole.CALL).all()

    elif current_user.role == UserRole.TEAM:
        return (
            db.query(Client)
            .join(User)
            .filter(User.role == UserRole.CALL, User.team_id == current_user.team_id)
            .all()
        )

    elif current_user.role == UserRole.CALL:
        return db.query(Client).filter(Client.user_id == current_user.id).all()

    return []
def get_current_user(username: str, db: Session = Depends(get_db)) -> models.User:
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

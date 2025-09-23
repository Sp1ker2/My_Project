from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from crm_app import crud, models, schemas
from crm_app.database import get_db

router = APIRouter(prefix="/users", tags=["users"])

# -----------------------------
# Получение текущего пользователя
# -----------------------------
def get_current_user(username: str, db: Session = Depends(get_db)) -> models.User:
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

# -----------------------------
# Admin создаёт команду + лидера
# -----------------------------
@router.post("/create_team_with_lead", response_model=schemas.UserBase)
def create_team_with_lead(
    data: schemas.TeamWithLeadCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(crud.get_current_user)
):
    if current_user.role != models.UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Not enough rights")

    existing_team = db.query(models.Team).filter(models.Team.name == data.team_name).first()
    if existing_team:
        raise HTTPException(status_code=400, detail="Team with this name already exists")

    team = models.Team(name=data.team_name, admin_id=current_user.id)
    db.add(team)
    db.commit()
    db.refresh(team)

    existing_user = db.query(models.User).filter(models.User.username == data.lead.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    lead = models.User(
        username=data.lead.username,
        password=data.lead.password,
        role=models.UserRole.TEAM,
        team_id=team.id
    )
    db.add(lead)
    db.commit()
    db.refresh(lead)

    return lead

# -----------------------------
# Team-лидер создаёт Call в своей команде
# -----------------------------
@router.post("/create_call_team", response_model=schemas.UserBase)
def create_call_for_team(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(crud.get_current_user)
):
    if current_user.role != models.UserRole.TEAM:
        raise HTTPException(status_code=403, detail="Not enough rights")

    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username already exists")

    new_user = models.User(
        username=user.username,
        password=user.password,
        role=models.UserRole.CALL,
        team_id=current_user.team_id
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    call_record = models.Call(
        user_id=new_user.id,
        team_id=current_user.team_id
    )
    db.add(call_record)
    db.commit()
    db.refresh(call_record)

    return new_user

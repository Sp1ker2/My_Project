import uvicorn
from fastapi import FastAPI
from crm_app.database import engine, Base
from crm_app.routers import clients, auth, users

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CRM FastAPI PostgreSQL")

app.include_router(auth.router)
app.include_router(clients.router)
app.include_router(users.router)
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

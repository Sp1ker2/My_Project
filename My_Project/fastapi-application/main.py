from contextlib import asynccontextmanager
from typing import AsyncIterator

import uvicorn
from fastapi import FastAPI
from core.config import settings
from api import router as api_router
from core.models import db_helper
from fastapi.responses import ORJSONResponse


@asynccontextmanager
async def lifespan(app:FastAPI) -> AsyncIterator[None]:
    # startup
    # async with db_helper.engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    yield
    # shutdown
    print("dispose")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan,default_response_class = ORJSONResponse )
main_app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run("main:main_app",host=settings.run.host,port=settings.run.port, reload=True)
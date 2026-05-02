from fastapi import FastAPI
from app.routes.health import router
from app.config import APP_NAME, APP_VERSION
from app.logger import setup_logger

logger = setup_logger()

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(router)


@app.on_event("startup")
async def startup_event():
    logger.info("Application started successfully")

from fastapi import APIRouter
from app.config import APP_NAME, APP_VERSION, ENVIRONMENT

router = APIRouter()


@router.get("/")
def root():
    return {
        "message": "Enterprise DevSecOps Platform API",
        "documentation": "/docs",
        "health_check": "/health"
    }


@router.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": APP_NAME,
        "version": APP_VERSION,
        "environment": ENVIRONMENT
    }


@router.get("/version")
def version():
    return {
        "version": APP_VERSION
    }


@router.get("/api/hello")
def hello():
    return {
        "message": "Welcome to Enterprise DevSecOps Platform"
    }

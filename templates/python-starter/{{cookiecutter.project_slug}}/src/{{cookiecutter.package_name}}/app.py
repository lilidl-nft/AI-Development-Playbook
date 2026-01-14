from contextlib import asynccontextmanager
from fastapi import FastAPI
from .logging import configure_logging
from .api import health

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    configure_logging()
    yield
    # Shutdown

def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    
    # Register Routers
    app.include_router(health.router, prefix="/api")
    
    return app

app = create_app()

from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as taks_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application start-up")
    yield
    print("Application shut-down")
    
app = FastAPI(lifespan=lifespan)

app.include_router(router=taks_routes)
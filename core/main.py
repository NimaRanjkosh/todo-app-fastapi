from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as task_routes
from taskstatus.routes import router as task_status_routes
from users.routes import router as users_routes


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application start-up")
    yield
    print("Application shut-down")
    
app = FastAPI(lifespan=lifespan)

app.include_router(router=task_routes, tags=["tasks"], prefix="/todo")
app.include_router(router=task_status_routes, tags=["taskstatus"], prefix="/todo")
app.include_router(router=users_routes, tags=["users"], prefix="/todo")
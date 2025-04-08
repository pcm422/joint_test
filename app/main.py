from fastapi import FastAPI
from app.domains.users.router import router as users_router
from app.core.config import ENVIRONMENT

app = FastAPI(title="My FastAPI Project", version="0.1.0")

@app.get("/")
async def root():
    return {"message": f"Hello World in {ENVIRONMENT} environment"}

# 도메인 라우터 포함
app.include_router(users_router, prefix="/api/users", tags=["users"])
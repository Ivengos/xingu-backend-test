from fastapi import FastAPI
from app.db.connection import init_db
from app.routes.routes import router as test_router

app = FastAPI()


# MongoDB Initialisierung
@app.on_event("startup")
async def on_startup():
    await init_db()


# include routes
app.include_router(test_router, prefix="/test")

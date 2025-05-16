from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import engine, base

app = FastAPI(title="GUIDE API", openapi_url="/openapi.json")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

base.Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Welcome to GUIDE API"}
from fastapi import FastAPI
from game.router import router as game_router
from fastapi.middleware.cors import CORSMiddleware

import uvicorn

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(game_router, prefix="/game", tags=["Game"])


from fastapi import FastAPI

from routes import morph_router

app = FastAPI()
app.include_router(morph_router)

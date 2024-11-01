import os

from fastapi import FastAPI

from routes import morph_router

app = FastAPI(root_path=os.getenv("MORPHER_ROOT_DIR"))
app.include_router(morph_router)

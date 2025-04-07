from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router
import os

app = FastAPI()

#API routes
app.include_router(router)

# Serve static frontend files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

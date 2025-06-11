from fastapi import FastAPI, Response
from fastapi.staticfiles import StaticFiles
from app.routes import router
import os

app = FastAPI()

# API routes
app.include_router(router)

# Serve favicon
@app.get("/favicon.ico")
async def get_favicon():
    with open("static/favicon.ico", "rb") as f:
        favicon = f.read()
    return Response(favicon, media_type="image/x-icon")

# Serve static frontend files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
app.mount("/", StaticFiles(directory=static_dir, html=True), name="static")

# Root check route
@app.get("/api/health")
def root():
    return {"message": "App is working"}

# Required to run on Railway
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)

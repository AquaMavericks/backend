from fastapi import FastAPI
from routers.port import port_router
from routers.admin import admin_router
from routers.robot import robot_router
app = FastAPI(prefix="v1/")

app.include_router(port_router.router)
app.include_router(admin_router.router)
app.include_router(robot_router.router)
@app.get("/")
async def root():
    return {"message": "Hello World"}
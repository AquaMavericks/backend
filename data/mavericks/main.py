from fastapi import FastAPI
from routers.port import port_router
app = FastAPI(prefix="v1/")

app.include_router(port_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
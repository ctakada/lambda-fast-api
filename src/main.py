from fastapi import FastAPI
from mangum import Mangum

from .utils.routes_loader import load_routers

app = FastAPI()
routers = load_routers()

for router in routers:
    app.include_router(router)

handler = Mangum(app)

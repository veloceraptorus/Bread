from typing import Optional
from fastapi import FastAPI
import uvicorn


from src.config import settings
from src.routes.basic_router import router


print(settings.WELCOME_MSG)

app = FastAPI(
    openapi_url=f"{settings.BASE_ROUTE_PATH}/openapi.json",
    docs_url=f"{settings.BASE_ROUTE_PATH}/docs",
)

app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

from fastapi import FastAPI

import uvicorn

app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
)

@app.get('/hello-world')
def hello_world():
    return "Hi mam!"

@app.get('/как-там-с-деньгами')
def gg():
    return "никак"

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

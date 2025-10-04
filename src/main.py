from typing import Optional
from fastapi import FastAPI
from .schemes.gvn import Govna, MisieGovna

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

@app.post('/post_endpoint')
def post_data(body: Govna) -> MisieGovna:
    misie_govna = MisieGovna(
        color=body.color,
        vkusnost=body.vkusnost,
        zvozd = body.vkusnost/3
    )
    return misie_govna

if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

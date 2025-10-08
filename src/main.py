from typing import Optional
from fastapi import FastAPI
from .schemes.gvn import Govna, MisieGovna, Car

import uvicorn
    
        
app = FastAPI(
    openapi_url="/openapi.json",
    docs_url="/docs",
)

# @app.get('/hello-world')
# def hello_world():
#     return "Hi mam!"

# @app.get('/как-там-с-деньгами')
# def gg():
#     return "никак"

@app.post('/kakish')
def post_data(body: Govna) -> MisieGovna:
    misie_govna = MisieGovna(
        color = body.color,
        vkusnost = body.vkusnost,
        zvozd = body.vkusnost/3
    )
    return misie_govna

@app.post('/Автомобили')
def car_inf(body: Car):
    ccaarr = Car(
        Марка = body.Марка,
        Цвет = body.Цвет,
        Пробег_км = body.Пробег_км,
        Количество_колёс_шт = body.Количество_колёс_шт,
        Вес_кг = body.Вес_кг,
        Год_выпуска = body.Год_выпуска,
        Скорость_кмч = body.Скорость_кмч
    )
    return ccaarr
if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        host='localhost',
        port=8000,
        reload=True,
    )

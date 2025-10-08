from fastapi.routing import APIRouter

from src.schemes.gvn import Govna, MisieGovna, Car
from src.config import settings

router = APIRouter(prefix=settings.BASE_ROUTE_PATH)

# @router.get('/hello-world')
# def hello_world():
#     return "Hi mam!"

# @router.get('/как-там-с-деньгами')
# def gg():
#     return "никак"

@router.post('/kakish')
def post_data(body: Govna) -> MisieGovna:
    misie_govna = MisieGovna(
        color = body.color,
        vkusnost = body.vkusnost,
        zvozd = body.vkusnost/3
    )
    return misie_govna

@router.post('/Автомобили')
def car_inf(body: Car):
    ccaarr = Car(**dict(body))
    # ccaarr = Car(
    #     Марка = body.Марка,
    #     Цвет = body.Цвет,
    #     Пробег_км = body.Пробег_км,
    #     Количество_колёс_шт = body.Количество_колёс_шт,
    #     Вес_кг = body.Вес_кг,
    #     Год_выпуска = body.Год_выпуска,
    #     Скорость_кмч = body.Скорость_кмч
    # )
    return ccaarr

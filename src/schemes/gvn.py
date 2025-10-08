from pydantic import BaseModel, Field

class Govna(BaseModel):
    von: bool = Field(default=True)
    color: str
    vkusnost: int = Field(ge=-3,le=10)
    count: int =  Field(ge=0, le=999)

class MisieGovna(BaseModel):
    von: bool = Field(default=True)
    color: str
    vkusnost: int
    zvozd: int
    
class Car(BaseModel):
    Марка: str 
    Цвет: str
    Пробег_км: int
    Количество_колёс_шт: int
    Вес_кг: int
    Год_выпуска: str
    Скорость_кмч: str
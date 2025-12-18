 from .collision import (# импорт функций и класса из модуля collision в текущем пакете
    isCorrectRect,           # проверяет корректность прямоугольника
    isCollisionRect,         # определяет столкновение двух прямоугольников
    intersectionAreaRect,    # вычисляет площадь пересечения двух прямоугольников
    intersectionAreaMultiRect, # вычисляет общую площадь пересечения нескольких прямоугольников
    RectCorrectError         # класс исключения для ошибок корректности прямоугольника
)
 
__all__ = [ # список публичных объектов, экспортируемых из этого модуля
    'isCorrectRect',
    'isCollisionRect',
    'intersectionAreaRect',
    'intersectionAreaMultiRect',
    'RectCorrectError'
]

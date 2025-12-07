"""
Пакет collision для работы с прямоугольниками.
"""

from .collision import (
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect,
    RectCorrectError
)

__all__ = [
    'isCorrectRect',
    'isCollisionRect',
    'intersectionAreaRect',
    'intersectionAreaMultiRect',
    'RectCorrectError'
]
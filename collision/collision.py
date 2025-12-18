 def isCorrectRect(rect):
    """
    проверяет корректность прямоугольника.
    
    Прямоугольник считается корректным, если:
    1. Имеет две точки
    2. x1 < x2 (левая граница левее правой)
    3. y1 < y2 (нижняя граница ниже верхней)
    
    Args:
        rect: список из двух кортежей [(x1, y1), (x2, y2)]
    
    Returns:
        bool: True если прямоугольник корректный, False в противном случае
    """
    try:
        # проверяем, что rect - это список из двух кортежей
        if not isinstance(rect, list) or len(rect) != 2:
            return False
        
        p1, p2 = rect
        
        # проверяем, что точки - это кортежи из двух чисел
        if (not isinstance(p1, tuple) or not isinstance(p2, tuple) or
            len(p1) != 2 or len(p2) != 2):
            return False
        
        # извлекаем координаты
        x1, y1 = p1
        x2, y2 = p2
        
        # проверяем, что это числа
        if not (isinstance(x1, (int, float)) and isinstance(y1, (int, float)) and
                isinstance(x2, (int, float)) and isinstance(y2, (int, float))):
            return False
        
        # проверяем, что левый нижний угол действительно левее и ниже правого верхнего
        return x1 < x2 and y1 < y2
        
    except (TypeError, ValueError):
        return False
    




class RectCorrectError(Exception):
    """Исключение для некорректных прямоугольников."""
    pass


def isCollisionRect(rect1, rect2):
    """
    Проверяет, пересекаются ли два прямоугольника.
    
    Args:
        rect1: первый прямоугольник [(x1, y1), (x2, y2)]
        rect2: второй прямоугольник [(x1, y1), (x2, y2)]
    
    Returns:
        bool: True если прямоугольники пересекаются, False в противном случае
    
    Raises:
        RectCorrectError: если передан некорректный прямоугольник
    """
    # проверяем корректность прямоугольников
    if not isCorrectRect(rect1):
        raise RectCorrectError("1й прямоугольник некоректный")  # обратите внимание на опечатку "некоректный" - как в задании
    if not isCorrectRect(rect2):
        raise RectCorrectError("2й прямоугольник некоректный")
    
    # извлекаем координаты
    (x1_1, y1_1), (x2_1, y2_1) = rect1
    (x1_2, y1_2), (x2_2, y2_2) = rect2
    
    # проверяем пересечение по осям X и Y
    intersect_x = not (x2_1 <= x1_2 or x2_2 <= x1_1)
    intersect_y = not (y2_1 <= y1_2 or y2_2 <= y1_1)
    
    return intersect_x and intersect_y





def intersectionAreaRect(rect1, rect2):
    """
    Вычисляет площадь пересечения двух прямоугольников.
    
    Args:
        rect1: первый прямоугольник [(x1, y1), (x2, y2)]
        rect2: второй прямоугольник [(x1, y1), (x2, y2)]
    
    Returns:
        float: площадь пересечения (0 если не пересекаются)
    
    Raises:
        ValueError: если передан некорректный прямоугольник
    """
    # проверяем корректность прямоугольников
    if not isCorrectRect(rect1):
        raise ValueError("Первый прямоугольник некорректный")
    if not isCorrectRect(rect2):
        raise ValueError("Второй прямоугольник некорректный")
    
    # проверяем пересечение
    if not isCollisionRect(rect1, rect2):
        return 0.0
    
    # извлекаем координаты
    (x1_1, y1_1), (x2_1, y2_1) = rect1
    (x1_2, y1_2), (x2_2, y2_2) = rect2
    
    # вычисляем координаты пересечения
    x_left = max(x1_1, x1_2)
    x_right = min(x2_1, x2_2)
    y_bottom = max(y1_1, y1_2)
    y_top = min(y2_1, y2_2)
    
    # вычисляем площадь пересечения
    width = x_right - x_left
    height = y_top - y_bottom
    
    return width * height




def intersectionAreaMultiRect(rectangles):
    """
    Вычисляет общую площадь пересечения всех прямоугольников.
    
    Args:
        rectangles: список прямоугольников [[(x1, y1), (x2, y2)], ...]
    
    Returns:
        float: общая площадь пересечения всех прямоугольников
    
    Raises:
        RectCorrectError: если передан некорректный прямоугольник
    """
    if not rectangles:
        return 0.0
    
    # проверяем корректность всех прямоугольников
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {i+1} некорректный")
    
    # если только один прямоугольник, возвращаем его площадь
    if len(rectangles) == 1:
        (x1, y1), (x2, y2) = rectangles[0]
        return (x2 - x1) * (y2 - y1)
    
    # для двух прямоугольников используем уже готовую функцию
    if len(rectangles) == 2:
        return intersectionAreaRect(rectangles[0], rectangles[1])
    
    # для трех и более прямоугольников используем метод сканирования по оси X
    # собираем все уникальные X координаты
    x_coords = set()
    for rect in rectangles:
        (x1, _), (x2, _) = rect
        x_coords.add(x1)
        x_coords.add(x2)
    
    # сортируем X координаты
    sorted_x = sorted(x_coords)
    
    total_area = 0.0
    
    # проходим по всем промежуткам между X координатами
    for i in range(len(sorted_x) - 1):
        x_left = sorted_x[i]
        x_right = sorted_x[i + 1]
        width = x_right - x_left
        
        if width <= 0:
            continue
        
        # находим Y координаты, где прямоугольники пересекаются в текущем X промежутке
        y_intervals = []
        
        for rect in rectangles:
            (x1, y1), (x2, y2) = rect
            
            # если прямоугольник пересекает текущий X промежуток
            if x1 <= x_left and x2 >= x_right:
                y_intervals.append((y1, y2))
        
        if not y_intervals:
            continue
        
        # находим пересечение всех Y интервалов
        y_intervals.sort()
        current_y_interval = y_intervals[0]
        
        for j in range(1, len(y_intervals)):
            y1_curr, y2_curr = current_y_interval
            y1_next, y2_next = y_intervals[j]
            
            # находим пересечение
            y_intersect_bottom = max(y1_curr, y1_next)
            y_intersect_top = min(y2_curr, y2_next)
            
            if y_intersect_bottom < y_intersect_top:
                current_y_interval = (y_intersect_bottom, y_intersect_top)
            else:
                # нет пересечения по Y
                current_y_interval = None
                break
        
        if current_y_interval:
            y_bottom, y_top = current_y_interval
            height = y_top - y_bottom
            total_area += width * height
    
    return total_area

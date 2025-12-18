from collision import (
    isCorrectRect,
    isCollisionRect,
    intersectionAreaRect,
    intersectionAreaMultiRect,
    RectCorrectError
)


def get_rect_input(n):
    # Запрос координат прямоугольника. 
    while True:
        print(f"\nПрямоугольник {n}:")
        try:
            x1 = float(input("x нижнего левого: "))
            y1 = float(input("y нижнего левого: "))
            x2 = float(input("x верхнего правого: "))
            y2 = float(input("y верхнего правого: "))
            
            rect = [(x1, y1), (x2, y2)]
            if isCorrectRect(rect):
                return rect
            print("Ошибка: x1 < x2 и y1 < y2!")
        except ValueError:
            print("Введите числа!")


def main():
    print("Демонстрация пакета collision")
    
    # примеры
    print("1. isCorrectRect:")
    tests = [
        [(-3.4, 1), (9.2, 10)],  # true
        [(-7, 9), (3, 6)],        # false
    ]
    for i, r in enumerate(tests, 1):
        print(f"   Пример {i}: {r} -> {isCorrectRect(r)}")
    
    print("\n2. isCollisionRect:")
    r1 = [(-3.4, 1), (9.2, 10)]
    r2 = [(-7.4, 0), (13.2, 12)]
    print(f"   {r1} и {r2} -> {isCollisionRect(r1, r2)}")
    
    print("\n3. intersectionAreaRect:")
    r3 = [(-3, 1), (9, 10)]
    r4 = [(-7, 0), (13, 12)]
    print(f"   {r3} и {r4} -> {intersectionAreaRect(r3, r4):.2f}")
    
    print("\n4. intersectionAreaMultiRect:")
    rects = [
        [(-3, 1), (9, 10)],
        [(-7, 0), (13, 12)],
        [(0, 0), (5, 5)],
    ]
    print(f"   {len(rects)} прямоугольника -> {intersectionAreaMultiRect(rects):.2f}")
    
    # интерактивная часть
    print("\n" + "="*40)
    print("Интерактивный режим:")
    
    while True:
        print("\n1 - Проверить прямоугольник")
        print("2 - Проверить столкновение")
        print("3 - Площадь пересечения 2-х")
        print("4 - Площадь пересечения N-х")
        print("0 - Выход")
        
        choice = input("Выбор: ")
        
        if choice == "1":
            rect = get_rect_input(1)
            print(f"Корректный: {isCorrectRect(rect)}")
        
        elif choice == "2":
            rect1 = get_rect_input(1)
            rect2 = get_rect_input(2)
            try:
                print(f"Пересекаются: {isCollisionRect(rect1, rect2)}")
            except RectCorrectError as e:
                print(f"Ошибка: {e}")
        
        elif choice == "3":
            rect1 = get_rect_input(1)
            rect2 = get_rect_input(2)
            try:
                area = intersectionAreaRect(rect1, rect2)
                print(f"Площадь пересечения: {area:.2f}")
            except ValueError as e:
                print(f"Ошибка: {e}")
        
        elif choice == "4":
            n = int(input("Сколько прямоугольников? "))
            rects = [get_rect_input(i+1) for i in range(n)]
            try:
                area = intersectionAreaMultiRect(rects)
                print(f"Общая площадь: {area:.2f}")
            except RectCorrectError as e:
                print(f"Ошибка: {e}")
        
        elif choice == "0":
            print("Выход.")
            break


if __name__ == "__main__":
    main()

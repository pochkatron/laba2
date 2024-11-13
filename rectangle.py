def area(a, b):
    '''
    Возвращает площадь прямоугольника 

        Параметры: 
            a (int): длина прямоугольника 
            b (int): ширина прямоугольника
        
        Возвращаемое значение:
            a * b: искомая площадь прямоугольника
    '''
    if a < 0 or b < 0:
        raise ValueError("Длина и ширина не могут быть отрицательными")
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника

        Параметры:
            a (int): длина прямоугольника
            b (int): ширина прямоугольника

        Возвращаемое значение:
            2 * (a + b): искомый периметр прямоугольника
    '''
    if a < 0 or b < 0:
        raise ValueError("Длина и ширина не могут быть отрицательными")
    return 2 * (a + b)
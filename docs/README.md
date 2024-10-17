# Математические формулы
## Нахождение площади
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Нахождение периметра
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Функции
## Круг
### Вычисление площади
*(r-радиус)*
```python
def area(r):
```
>Пример вызова: area(5) -> 78.53981633974483

### Вычисление периметра
*(r-радиус)*
```python
def perimeter(r):
```
>Пример вызова perimeter(5) -> 31.41592653589793

## Прямоугольник
### Вычисление площади
*(a,b-стороны прямоугольника)*
```python
def area(a,b):
```
> Пример вызова: area(3,4) -> 12

### Вычисление периметра
*(a,b-стороны прямоугольника)*
```python
def perimeter(a,b):
```
>Пример вызова: perimeter(3,4) -> 14

## Квадрат 
### Вычисление площади
*(a-сторона квадрата)*
```python
def area(a):
```
> Пример вызова: area(3) -> 9

### Вычисление периметра 
*(а-сторона квадрата)*
```python
def perimeter(a):
```
>Пример вызова: perimeter(3) -> 12

## Треугольник
### Вычисление площади
*(a-основание, h-высота)*
```python
def area(a,h):
```

> Пример вызова: area(3,4) -> 6

### Вычисление периметра 
*(a,b,c-стороны треугольника)*
```python
def perimeter(a,b,c):
```
>Пример вызова: perimeter (3,4,5) -> 12

# Changelog 
- [Fixed rectangle.py](https://github.com/pochkatron/geometric_lib/commit/d8409b63db5ce9468976e9f46a8d7179a23371a5)
- [Added triangle.py](https://github.com/pochkatron/geometric_lib/commit/ff15425b4dd4d19c31d2445477e5536859912ec7)
- [L-03:Circle and square added](https://github.com/pochkatron/geometric_lib/commit/a9296073e5854711d12beedf55c6e9f81fddb606)
- [;-03: Docs added](ttps://github.com/pochkatron/geometric_lib/commit/37a11b8c2be2325041760abde5f4e2b420cebe6d)
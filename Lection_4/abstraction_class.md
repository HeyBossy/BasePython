В объектно-ориентированном программировании (ООП) **абстрактный класс** в Python — это класс, который служит шаблоном для создания других классов. Он не предназначен для создания экземпляров напрямую и обычно содержит одно или несколько абстрактных методов, которые должны быть реализованы в дочерних классах.

Особенности абстрактного класса:
- Абстрактный класс определяется с помощью модуля abc (Abstract Base Classes).
- Абстрактные методы объявляются с использованием декоратора @abstractmethod.
- Астрактный класс может содержать как абстрактные, так и обычные методы.
- дочерние классы должны реализовать все абстрактные методы, чтобы стать конкретными (неабстрактными).
- Пример абстрактного класса:
```python

from abc import ABC, abstractmethod

# Определение абстрактного класса
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Класс, наследующий абстрактный класс
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Реализация метода area
    def area(self):
        return self.width * self.height

    # Реализация метода perimeter
    def perimeter(self):
        return 2 * (self.width + self.height)

# Использование
rect = Rectangle(5, 10)
print("Площадь:", rect.area())
print("Периметр:", rect.perimeter())

# Ошибка при попытке создать экземпляр абстрактного класса
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape with abstract me
```
"""
Модуль для работы с классом IsoscelesTriangle (Равнобедренный треугольник).
Реализует расчет площади, периметра и проверку существования.
"""
import math

class IsoscelesTriangle:
    def __init__(self, base, side):
        self._base = float(base)
        self._side = float(side)

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, value):
        if value <= 0:
            raise ValueError("Сторона должна быть положительной")
        self._base = value

    @property
    def side(self):
        return self._side

    @side.setter
    def side(self, value):
        if value <= 0:
            raise ValueError("Сторона должна быть положительной")
        self._side = value

    def is_exists(self):
        """Проверка существования: сумма двух сторон больше третьей"""
        a, b = self._base, self._side
        return 2 * self._side > self._base > 0 and self._side > 0

    def get_perimeter(self):
        if not self.is_exists():
            return 0
        return self._base + 2 * self._side

    def get_area(self):
        if not self.is_exists():
            return 0
        # Высота по теореме Пифагора: h = sqrt(side^2 - (base/2)^2)
        h = math.sqrt(self._side**2 - (self._base / 2)**2)
        return 0.5 * self._base * h

    def __str__(self):
        if self.is_exists():
            return "Равнобедренный треугольник (основание={self._base}, бедра={self._side})"
        return "Треугольник с такими сторонами не существует"

    def __eq__(self, other):
        if not isinstance(other, IsoscelesTriangle):
            return False
        return self._base == other._base and self._side == other._side

# Интерактивная часть
print("--- Тестирование класса Треугольник ---")
b1 = input("Введите основание треугольника 1: ")
s1 = input("Введите боковую сторону треугольника 1: ")
tri1 = IsoscelesTriangle(b1, s1)

b2 = input("Введите основание треугольника 2: ")
s2 = input("Введите боковую сторону треугольника 2: ")
tri2 = IsoscelesTriangle(b2, s2)

while True:
    print("\nМЕНЮ:")
    print("1. Показать данные (T1: {tri1})")
    print("2. Расчитать периметр и площадь T1")
    print("3. Проверить существование T1")
    print("4. Сравнить T1 и T2")
    print("0. Выход")

    choice = input("\nВыберите действие: ")

    if choice == "1":
        print("T1: {tri1}")
        print("T2: {tri2}")
    elif choice == "2":
        print("Периметр T1: {tri1.get_perimeter()}")
        print("Площадь T1: {tri1.get_area():.2f}")
    elif choice == "3":
        msg = "Существует" if tri1.is_exists() else "Не существует"
        print("Результат: {msg}")
    elif choice == "4":
        print("Равны ли треугольники?: {tri1 == tri2}")
    elif choice == "0":
        break

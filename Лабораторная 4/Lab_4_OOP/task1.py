class Weapon:
    """Базовый класс для оружия"""

    def __init__(self, name: str, durability: int):
        """Конструктор объектов класса Weapon"""
        if not isinstance(name, str):
            raise TypeError(f"Имя оружия должно быть строкой, а не {type(name)}")
        if not isinstance(durability, int):
            raise TypeError(f"Прочность оружия должна быть целым числом, а не {type(name)}")
        if durability <= 0:
            raise ValueError("Изначальная прочность оружия должна быть больше 0")
        self._name = name  # атрибут открыт только для чтения так как имя оружия не надо менять после его иницализации
        self._durability = durability  # атрибут открыт только для чтения так как за изменение прочность ответсвенны
        # соотвествующие методы внутри класса

    # Геттеры (read only атрибуты)
    @property
    def name(self) -> str:
        """Возвращает имя оружия"""
        return self._name

    @property
    def durability(self) -> int:
        """Возвращает текущую прочность оружия"""
        return self._durability

    # Методы экземпляров класса
    def __str__(self):
        return f"Оружие {self.name}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, durability={self.durability})"

    def weapon_break(self) -> None:
        """Метод срабатывающий при поломке оружия"""
        ...

    def reduce_durability(self) -> None:
        """Метод уменьшающий прочность оружия после его использования"""
        ...


class HeavyWeapon(Weapon):
    """Класс для тяжёлого вооружения"""

    def __init__(self, name: str, durability: int):
        """Конструктор объектов класса HeavyWeapon"""
        super().__init__(name, durability)

    # Методы экземпляров класса
    def __str__(self):
        return f"Тяжёлое оружие {self.name}."

    def reduce_durability(self) -> None:
        """Метод уменьшающий прочность тяжёлого оружия после его использования
        (перегружен так как по задумке формулы для расчёта прочности обычного
        и тяжёлого оружия различны)"""
        ...


class RangeWeapon(Weapon):
    """Класс для дальнобойного вооружения"""

    def __init__(self, name: str, durability: int, distance: int = 0):
        """Конструктор объектов класса RangeWeapon"""
        super().__init__(name, durability)
        self.distance = distance  # доступ к атрибуту distance реализуется через сеттер и геттер для уменьшения
        # количества возможных ошибок при взаимодействии с ним

    # Сеттеры и геттеры
    @property
    def distance(self) -> int:
        """Возвращает заданную дистанцию до цели"""
        return self._distance

    @distance.setter
    def distance(self, new_distance: int) -> None:
        """Устанавливает дистанцю до цели"""
        if not isinstance(new_distance, int):
            raise TypeError("расстояние до цели должно быть целым чисолом")
        if new_distance < 0:
            raise ValueError("расстояние до цели должно быть положительным числом")
        self._distance = new_distance

    # Методы экземпляров класса

    def __str__(self):
        return f"Дальнобойное оружие {self.name}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, durability={self.durability}, distance={self.distance})"

    def reduce_durability(self) -> None:
        """Метод уменьшающий прочность дальнобойного оружия после его использования
        (перегружен так как по задумке формулы для расчёта прочности обычного
        и дальнобойного оружия различны)"""
        ...


def main() -> None:
    sword = Weapon("Gladius", 100)
    heavy_sword = HeavyWeapon("Flamberge", 200)
    bow = RangeWeapon("Longbow", 150)
    print(sword, heavy_sword, bow)
    print(repr(sword), repr(heavy_sword), repr(bow))
    bow.distance = 100
    print(repr(bow))


if __name__ == "__main__":
    # Write your solution here
    main()
    pass

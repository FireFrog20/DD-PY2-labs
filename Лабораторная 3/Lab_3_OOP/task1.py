class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        """Конструктор объектов класса Book"""
        if not isinstance(name, str):
            raise TypeError(f"Имя книги должно быть строкой, а не {type(name)}")
        if not isinstance(author, str):
            raise TypeError(f"ФИО автора должно быть строкой, а не {type(author)}")
        self._name = name
        self._author = author

    # Геттеры (read only атрибуты)
    @property
    def name(self) -> str:
        """Возвращает имя книги"""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает ФИО автора книги"""
        return self._author

    # Методы экземпляров класса
    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс для описания бумажных книг"""

    def __init__(self, name: str, author: str, pages: int):
        """Конструктор объектов класса PaperBook"""
        super().__init__(name, author)
        self.pages = pages

    # Сеттеры и геттеры
    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает значение количества страниц в книге"""
        if not isinstance(new_pages, int):
            raise TypeError("количество страниц должно быть целочисленным")
        if new_pages <= 0:
            raise ValueError("количество страниц должно быть положительным числом")
        self._pages = new_pages

    # Методы экземпляров класса
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages})"


class AudioBook(Book):
    """Класс для описания аудиокниг"""

    def __init__(self, name: str, author: str, duration: float):
        """Конструктор объектов класса AudioBook"""
        super().__init__(name, author)
        self.duration = duration

    # Сеттеры и геттеры
    @property
    def duration(self) -> float:
        """Возвращает длительность книги"""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает длительность аудиокниги"""
        if not isinstance(new_duration, (int, float)):
            raise TypeError("длительность аудиокниги должна быть целым числом или числом с плавющей точкой")
        if new_duration <= 0:
            raise ValueError("длительность аудиокниги должна быть положительным числом")
        self._duration = new_duration

    # Методы экземпляров класса
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration})"


def main() -> None:
    ...


if __name__ == '__main__':
    main()

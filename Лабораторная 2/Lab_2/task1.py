BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    """Класс для описания книг"""

    def __init__(self, id_: int, name_: str, pages_: int):
        """Конструктор объектов клвсса Book"""
        self.id = id_
        self.name = name_
        self.pages = pages_

    # Геттеры и сеттеры для атрибутов
    @property
    def id(self) -> int:
        """Возвращает id книги"""
        return self._id

    @id.setter
    def id(self, new_id: int) -> None:
        """Устанавливает значение id книги"""
        if not isinstance(new_id, int):
            raise TypeError("id должно быть типа int")
        if new_id <= 0:
            raise ValueError("id должно быть положительным числом")
        self._id = new_id

    @property
    def name(self) -> str:
        """Возвращает имя книги"""
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        """Устанавливает значение имени книги"""
        if not isinstance(new_name, str):
            raise TypeError("имя книги должно быть типа str")
        self._name = new_name

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает значение количества страниц в книге"""
        if not isinstance(new_pages, int):
            raise TypeError("количество страниц должно быть типа int")
        if new_pages < 0:
            raise ValueError("количество страниц должно быть положительным числом")
        self._pages = new_pages

    # Методы экземпляров класса
    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(id_={self.id}, name={self.name!r}, pages={self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name_=book_dict["name"], pages_=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__

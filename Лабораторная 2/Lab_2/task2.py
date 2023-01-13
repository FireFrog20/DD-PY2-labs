from typing import List

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


# TODO написать класс Library

class Library:
    """Класс для описания библиотек"""

    def __init__(self, books_: List[Book] = None):
        """Конструктор объектов клвсса Library"""
        if books_ is None:
            books_ = []
        self.books = books_

    # Геттеры и сеттеры для атрибутов
    @property
    def books(self) -> List[Book]:
        """Возвращает список книг, хранящихся в библиотеке"""
        return self._books

    @books.setter
    def books(self, new_books: List[Book]) -> None:
        """Устанавливает список книг, хранящихся в библиотеке"""
        if not (isinstance(new_books, list) and all([isinstance(item, Book) for item in new_books])) and new_books:
            raise TypeError("список книг должен быть типа list[Book]")
        self._books = new_books

    # Методы экземпляров класса
    def get_next_book_id(self) -> int:
        """Метод, возвращающий идентификатор для добавления новой книги в библиотеку"""
        if not self.books:
            return 1
        else:
            return self._books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """Метод, возвращающий индекс книги в списке по её id"""
        if not isinstance(book_id, int):
            raise TypeError("id должно быть типа int")

        id_list = [book.id for book in self.books]

        if book_id not in id_list:
            raise ValueError("Книги с запрашиваемым id не существует")
        return id_list.index(book_id)


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name_=book_dict["name"], pages_=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books_=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1

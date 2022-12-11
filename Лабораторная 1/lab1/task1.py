import doctest


# Класс описывающий работы COM порта
class Serial:
    """
    Класс для работы с COM портом
    """

    def __init__(self):
        """
        Конструктор объектов класса Serial
        __port_list - список доступных в системе COM портов
        __speed - скорость обмена данными
        __current_port - Порт используемого для работы COM порта
        Примеры:
        >>> serial = Serial() # инициализация экземпляра класса
        """
        self.__port_list = None
        self.__speed = None
        self.__current_port = None

        self.refresh_port_list()  # Обновляем список доступных портов
        ...

    def __browse_ports(self) -> list:
        """
        Функция поиска доступных COM портов
        :return: список доступных COM портов
        """
        ...

    def refresh_port_list(self) -> None:
        """
        Метод для обновления списка доступных COM портов
        Примеры:
        >>> serial = Serial() # инициализация экземпляра класса
        >>> serial.refresh_port_list() # обновление
        """
        self.__port_list = self.__browse_ports()

    def set_serial_speed(self, speed: int) -> None:
        """
        Сеттер для параметра speed класса Serial
        :param speed: задаваеммая скорость обмена данными
        Примеры:
        >>> serial = Serial() # инициализация экземпляра класса
        >>> serial.set_serial_speed(2000) # установка параметра speed
        """
        if not isinstance(speed, int):
            raise TypeError("Скорость порта должна быть целым числом")
        if not speed > 0:
            raise ValueError("Скорость порта должны быть больше 0")
        self.__speed = speed

    def set_serial_port(self, port: int) -> None:
        """
        Сеттер для параметра current_port класса Serial
        :param port: адаваемое значение порта
        Примеры:
        >>> serial = Serial() # инициализация экземпляра класса
        >>> serial.set_serial_port(1111) # установка параметра current port
        """
        if not isinstance(port, int):
            raise TypeError("Значение порта должно быть целым числом")
        if not port > 0 or port > 9999:
            raise ValueError("Значение порта должны быть больше 0 и меньше 9999")
        self.__current_port = port

    def set_serial_port_from_list(self, n: int) -> None:
        """
        Функция для задания current_port значения n-го порта из списка доступных COM портов
        :param n: номер нужного порта в списке
        Примеры:
        >>> serial = Serial() # инициализация экземпляра класса

        # проверка функции трудноосущиствима так как предполагается, что port_list заполняется информацией,
        # предоставляемой методом browse_ports, который на данный момент не реализован
        """
        self.refresh_port_list()
        if len(self.__port_list) == 0:
            raise ValueError("Список портов пуст")
        if not isinstance(n, int):
            raise TypeError("Номер порта должен быть целым числом")
        if n < 0:
            raise ValueError("Номер порта должен быть положительным числом")
        if n > len(self.__port_list):
            raise ValueError("Номер порта выходит за пределы списка портов")
        self.set_serial_port(self.__port_list[n])

    def get_serial_port_list(self) -> list:
        """
                Геттер для параметра port_list класса Serial
                :return: значение port_list
                Примеры:
                >>> serial = Serial() # инициализация экземпляра класса
                >>> portlist = serial.get_serial_port_list() # доступ к параметру port_list
                """
        self.refresh_port_list()
        return self.__port_list

    def get_serial_port(self) -> int:
        """
                Геттер для параметра current_port класса Serial
                :return: значение current_port
                Примеры:
                >>> serial = Serial() # инициализация экземпляра класса
                >>> port = serial.get_serial_port() # доступ к параметру current_port
                """
        return self.__current_port

    def get_serial_speed(self) -> int:
        """
                Геттер для параметра speed класса Serial
                :return: значение speed
                Примеры:
                >>> serial = Serial() # инициализация экземпляра класса
                >>> speed = serial.get_serial_speed() # доступ к параметру speed
                """
        return self.__speed

    def start(self) -> None:
        """
        Функция запуска  обмена данными через порт
        Примеры:
        >>> serial = Serial() # инициализация экземпляра класса
        >>> serial.start() # старт обмена данными через COM порт
        """
        ...


# Класс описывающий ванны
class Bath:
    """
    Класс для описания ванн
    """

    def __init__(self):
        """Конструктор объектов класса Bath
        __volume - объем ванны
        __color - цвет ванны
        __liquid_volume - объем воды в ванне
        Примеры:
        >>> bath = Bath() # инициализация экземпляра класса"""
        self.__volume = None
        self.__color = None
        self.__liquid_volume = None

    def set_bath_volume(self, volume: float) -> None:
        """
        Сеттер для параметра volume класса Bath
        :param volume: задаваемый объем ванны
        Примеры:
        >>> bath = Bath() # инициализация экземпляра класса
        >>> bath.set_bath_volume(200) # установка параметра volume
        """
        if not isinstance(volume, (int, float)):
            raise TypeError("Объем ванны должен быть числом")
        if not volume > 0:
            raise ValueError("Объем ванны должен быть больше 0")
        self.__volume = volume

    def set_liquid_volume(self, liquid_volume: float) -> None:
        """
        Сеттер для параметра liquid_volume класса Bath
        :param liquid_volume: задаваемый объем жидкости
        Примеры:
        >>> bath = Bath() # инициализация экземпляра класса
        >>> bath.set_bath_volume(200)
        >>> bath.set_liquid_volume(100) # установка параметра liquid_volume
        """
        if not isinstance(liquid_volume, (int, float)):
            raise TypeError("Объем ванны должен быть числом")
        if liquid_volume < 0:
            raise ValueError("Объем заливаемой жидкости должен быть положительным числом")
        if liquid_volume > self.__volume:
            raise ValueError("Объем заливаемой жидкости должен быть меньше обема ванны")
        self.__liquid_volume = liquid_volume

    def set_bath_color(self, color: str) -> None:
        """
        Сеттер для параметра color класса Bath
        :param color: задаваемый цвет ванны
        Примеры:
        >>> bath = Bath() # инициализация экземпляра класса
        >>> bath.set_bath_color("white") # установка параметра color
        """
        if not isinstance(color, str):
            raise TypeError("Цвет ванны должен быть строкой")
        self.__color = color

    def get_bath_volume(self) -> float:
        """
                Геттер для параметра volume класса Bath
                :return: значение volume
                Примеры:
                >>> bath = Bath() # инициализация экземпляра класса
                >>> volume = bath.get_bath_volume() # доступ к параметру volume
                """
        return self.__volume

    def get_liquid_volume(self) -> float:
        """
                Геттер для параметра liquid_volume класса Bath
                :return: значение liquid_volume
                Примеры:
                >>> bath = Bath() # инициализация экземпляра класса
                >>> liquid_volume = bath.get_liquid_volume() # доступ к параметру liquid_volume
                """
        return self.__liquid_volume

    def get_bath_color(self) -> str:
        """
                Геттер для параметра color класса Bath
                :return: значение color
                Примеры:
                >>> bath = Bath() # инициализация экземпляра класса
                >>> color = bath.get_bath_color() # доступ к параметру color
                """
        return self.__color

    def fill(self, vol: float) -> None:
        """
        Функция наполнения ванны водой
        :param vol: объем вливаемой жидкости
        Примеры:
        >>> bath = Bath() # инициализация экземпляра класса
        >>> bath.fill(100) # заливаем в ванну 100 ед жидкости
        """
        ...

    def drain(self, vol: float) -> None:
        """
        Функция осушения ванны
        :param vol: объем удаляемой жидкости
        Примеры:
        >>> bath = Bath() # инициализация экземпляра класса
        >>> bath.fill(10) # удаляем из ванны 10 ед жидкости
        """
        ...


# Класс описывающий книги
class Book:
    """
    Класс для описания книг
    """

    def __init__(self):
        """Конструктор объектов класса Book
        __words - количество слов
        __color - цвет книги
        __title - название книги
        Примеры:
        >>> book = Book() # инициализация экземпляра класса"""
        self.__words = None
        self.__color = None
        self.__title = None

    def set_words_amount(self, words: int) -> None:
        """
        Сеттер для параметра words класса Book
        :param words: задаваемое количество слов
        Примеры:
        >>> book = Book() # инициализация экземпляра класса
        >>> book.set_words_amount(150000) # установка параметра volume
        """
        if not isinstance(words, int):
            raise TypeError("Количество слов должно быть числом")
        if not words > 0:
            raise ValueError("Количество слов должно быть больше 0")
        self.__words = words

    def set_book_title(self, title: str) -> None:
        """
        Сеттер для параметра title класса Book
        :param title: задаваемое название книги
        Примеры:
        >>> book = Book() # инициализация экземпляра класса
        >>> book.set_book_title("Red like Roses") # установка параметра title
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.__title = title

    def set_book_color(self, color: str) -> None:
        """
        Сеттер для параметра color класса Book
        :param color: задаваемый цвет книги
        Примеры:
        >>> book = Book() # инициализация экземпляра класса
        >>> book.set_book_color("Red") # установка параметра color
        """
        if not isinstance(color, str):
            raise TypeError("Цвет книги должен быть строкой")
        self.__color = color

    def get_words_amount(self) -> int:
        """
                Геттер для параметра words класса Book
                :return: значение words
                Примеры:
                >>> book = Book() # инициализация экземпляра класса
                >>> words = book.get_words_amount() # доступ к параметру words
                """
        return self.__words

    def get_book_title(self) -> str:
        """
                Геттер для параметра title класса Book
                :return: значение title
                Примеры:
                >>> book = Book() # инициализация экземпляра класса
                >>> title = book.get_book_title() # доступ к параметру title
                """
        return self.__title

    def get_book_color(self) -> str:
        """
                Геттер для параметра color класса Book
                :return: значение color
                Примеры:
                >>> book = Book() # инициализация экземпляра класса
                >>> color = book.get_book_color() # доступ к параметру color
                """
        return self.__color

    def readline(self) -> str:
        """
        Функция чтения строки из книги. Перемещает указатель на следующую строку
        :return: Строка из книги
        Примеры:
        >>> book = Book() # инициализация экземпляра класса
        >>> line = book.readline() # Читаем строку из книги
        """
        ...

    def writeline(self, line: str) -> None:
        """
        Функция записи строки в книгу
        :param line: записывемая строка
        Примеры:
        >>> book = Book() # инициализация экземпляра класса
        >>> book.writeline("Red like roses fills my dreams") # записываем строку в книгу
        """
        ...


def main():
    doctest.testmod()


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    main()
    pass

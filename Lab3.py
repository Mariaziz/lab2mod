class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = None
        self.pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise ValueError("Указано не целое число страниц")
        if value <= 0:
            raise ValueError("Число страниц не может быть меньше нуля")
        self._pages = value

    def __str__(self):
        return f"Бумажная {super().__str__()}. Количество страниц: {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = None
        self.duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Введите численное значение длинтельности")
        if value <= 0:
            raise ValueError("Значение должно быть больше нуля")
        self._duration = value

    def __str__(self):
        return f"Аудио {super().__str__()}. Продолжительность: {self.duration} часов"
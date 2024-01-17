from math import ceil
from .base import PageCraftBase
from .page import Page

try:
    from sqlalchemy.orm import Query
except ImportError:
    raise ImportError("Debe instalar sqlalchemy: pip install sqlalchemy")


class PageCraftAlchemy(PageCraftBase):
    def __init__(self, query: Query, items=10) -> None:
        self.items = items
        self._query = query
        self._total_objects = self._query.order_by(None).count()

    def page(self, number: int):
        if not isinstance(number, int):
            raise TypeError("Argument number must be integer type.")

        if number > self.total_pages or number <= 0:
            return Page()

        self.number = number

        self._data = (
            self._query.limit(self.items).offset((self.number - 1) * self.items).all()
        )

        return Page(
            number=self.number,
            data=self._data,
            next_page=self.number + 1 if self.__has_next else None,
            prev_page=self.number - 1 if self.__has_prev else None,
        )

    @property
    def __has_next(self):
        return self.number in range(self.total_pages)

    @property
    def __has_prev(self):
        return self.number > 1

    @property
    def total_objects(self):
        return self._total_objects

    @property
    def total_pages(self):
        return ceil(self.total_objects / self.items)

    @total_pages.setter
    def total_pages(self):
        raise ValueError("Cannot set a new value")

    @total_objects.setter
    def total_objects(self):
        raise ValueError("Cannot set a new value")

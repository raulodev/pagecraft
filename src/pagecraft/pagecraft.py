from math import ceil
from .base import PageCraftBase
from .page import Page


class PageCraft(PageCraftBase):
    def __init__(
        self,
        list_objects: list,
        items: int = 10,
    ):
        """
        Args:
            list_objects (list)
            items (int, optional): Amount of data returned in page.data. Defaults to 5.
        """
        self.list_objects = list_objects
        self.items = items
        self.number = None
        self.list_pages = self.__create_pages()

    def page(self, number: int) -> Page:
        """Return the page

        Args:
            number (int): page number to get
        """
        if not isinstance(number, int):
            raise TypeError("Argument number must be integer type.")

        if number > self.total_pages or number <= 0:
            return Page()

        self.number = number

        self._data = self.list_pages[self.number - 1]

        return Page(
            number=self.number,
            data=self._data,
            next_page=self.number + 1 if self.__has_next else None,
            prev_page=self.number - 1 if self.__has_prev else None,
        )

    @property
    def total_objects(self) -> int:
        return len(self.list_objects)

    @property
    def total_pages(self) -> int:
        return ceil(self.total_objects / self.items)

    def __create_pages(self):
        pages = []
        for i in range(0, self.total_objects, self.items):
            page = self.list_objects[i : i + self.items]
            pages.append(page)
        return pages

    @property
    def __has_next(self):
        return self.number in range(self.total_pages)

    @property
    def __has_prev(self):
        return self.number > 1

    @total_pages.setter
    def total_pages(self):
        raise ValueError("Cannot set a new value")

    @total_objects.setter
    def total_objects(self):
        raise ValueError("Cannot set a new value")

from math import ceil
from .page import Page


class PageCraft:
    def __init__(
        self,
        object_list: list,
        items: int = 5,
    ):
        """Constructor para crear la paginación

        Args:
            object_list (list): Una lista de objetos
            items (int, optional): cantidad de elementos que debe devolver al llamar
            a la método page por defecto es 5.
        """
        self.object_list = object_list
        self.items = items
        self.number = None
        self.list_pages = self.__create_pages()

    def page(self, number: int) -> Page:
        """Retorna una página

        Args:
            number (int): número de la página ha obtener
        """
        if not isinstance(number, int):
            raise ValueError("El argumento debe ser de tipo entero")

        if number > self.total_pages or number <= 0:
            return Page()

        self.number = number - 1

        return Page(
            number=self.number + 1,
            data=self.list_pages[self.number],
            next_page=self.number + 2 if self.__has_next else None,
            prev_page=self.number if self.__has_prev else None,
        )

    @property
    def total_objects(self) -> int:
        """Retorna el número de objetos en total"""
        return len(self.object_list)

    @property
    def total_pages(self) -> int:
        "Retorna la cantidad de páginas en total"
        return ceil(self.total_objects / self.items)

    def __create_pages(self):
        pages = []
        for i in range(0, self.total_objects, self.items):
            page = self.object_list[i : i + self.items]
            pages.append(page)
        return pages

    @property
    def __has_next(self):
        return self.number in range(self.total_pages - 1)

    @property
    def __has_prev(self):
        return self.number - 1 in range(self.total_pages)

    @total_pages.setter
    def total_pages(self):
        raise ValueError("No se puede establecer un nuevo valor")

    @total_objects.setter
    def total_objects(self):
        raise ValueError("No se puede establecer un nuevo valor")

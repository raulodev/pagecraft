import json


class Page:
    def __init__(
        self,
        number: int = None,
        data: list = [],
        next_page: int = None,
        prev_page: int = None,
    ):
        self.number = number
        self.data = data
        self.next_page = next_page
        self.prev_page = prev_page

    def __default(self, obj_list: list):
        if isinstance(obj_list, list):
            return [str(obj) for obj in obj_list]

    def __str__(self) -> str:
        return str(
            json.dumps(
                {
                    "_": self.__class__.__name__,
                    "number": self.number,
                    "data": self.__default(self.data),
                    "next_page": self.next_page,
                    "prev_page": self.prev_page,
                    "is_exist": self.is_exist,
                },
                indent=4,
            )
        )

    @property
    def is_exist(self):
        return self.number is not None

    @property
    def has_next_page(self):
        return bool(self.next_page)

    @property
    def has_prev_page(self):
        return bool(self.prev_page)

    @is_exist.setter
    def is_exist(self):
        raise ValueError("No se puede establecer un nuevo valor")

    @has_next_page.setter
    def has_next_page(self):
        raise ValueError("No se puede establecer un nuevo valor")

    @has_prev_page.setter
    def has_prev_page(self):
        raise ValueError("No se puede establecer un nuevo valor")

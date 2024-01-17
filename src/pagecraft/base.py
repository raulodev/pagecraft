from abc import ABC, abstractmethod
from typing import Union, List


class PageBase(ABC):
    @abstractmethod
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

    @abstractmethod
    def __str__(self):
        pass

    @property
    @abstractmethod
    def is_exist(self):
        pass

    @property
    @abstractmethod
    def has_next_page(self):
        pass

    @property
    @abstractmethod
    def has_prev_page(self):
        pass


class PageCraftBase(ABC):
    @abstractmethod
    def page(self):
        pass

    @abstractmethod
    def total_objects(self):
        pass

    @abstractmethod
    def total_pages(self):
        pass

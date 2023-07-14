from abc import ABC, abstractmethod


class Figure(ABC):

    def add_area(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_area() + other_figure.get_area()
        raise ValueError

    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

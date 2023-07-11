from abc import ABC, abstractmethod


class Figure(ABC):

    def add_square(self, other_figure):
        if isinstance(other_figure, Figure):
            return self.get_square() + other_figure.get_square()
        raise ValueError

    @abstractmethod
    def get_square(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

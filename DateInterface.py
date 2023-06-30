from abc import ABC, abstractmethod

class DateInterface(ABC):
    @abstractmethod
    def display_date(self):
        pass

    @abstractmethod
    def display_day(self):
        pass

    @abstractmethod
    def display_month(self):
        pass

    @abstractmethod
    def display_year(self):
        pass
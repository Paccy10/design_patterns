from abc import ABC, abstractmethod


class Iterator(ABC):

    @abstractmethod
    def next(self):
        pass

    @abstractmethod
    def hasNext(self) -> bool:
        pass

    @abstractmethod
    def current(self):
        pass

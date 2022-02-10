from .iterator import Iterator


class BrowserHistory:
    __urls = []

    def push(self, url: str):
        self.__urls.append(url)

    def pop(self) -> str:
        return self.__urls.pop()

    def create_iterator(self) -> Iterator:
        return self.ListIterator(self)

    def get_urls(self):
        return self.__urls

    class ListIterator(Iterator):

        __history = None
        __index = 0

        def __init__(self, history):
            self.__history = history

        def hasNext(self) -> bool:
            return self.__index < len(self.__history.get_urls())

        def current(self):
            return self.__history.get_urls()[self.__index]

        def next(self):
            self.__index += 1

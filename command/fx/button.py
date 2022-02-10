from .command import Command

class Button:

    __label = ""
    __command = None

    def __init__(self, command: Command):
        self.__command = command

    def click(self):
        self.__command.execute()

    def get_lable(self):
        return self.__label

    def set_label(self, label: str):
        self.__label = label

from .tool import Tool


class Canvas:
    __current_tool = None

    def mouse_down(self):
        self.__current_tool.mouse_down()

    def mouse_up(self):
        self.__current_tool.mouse_up()

    def get_current_tool(self) -> Tool:
        return self.__current_tool

    def set_current_tool(self, current_tool: Tool):
        self.__current_tool = current_tool

class EditorState:
    __content = None

    def __init__(self, content):
        self.__content = content

    def get_content(self):
        return self.__content

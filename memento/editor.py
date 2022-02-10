from .editor_state import EditorState


class Editor:
    __content = None

    def create_state(self) -> EditorState:
        return EditorState(self.__content)

    def restore(self, state: EditorState):
        self.__content = state.get_content()

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

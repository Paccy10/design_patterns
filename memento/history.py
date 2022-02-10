from .editor_state import EditorState


class History:
    __states = []

    def push(self, state: EditorState):
        self.__states.append(state)

    def pop(self) -> EditorState:
        return self.__states.pop()

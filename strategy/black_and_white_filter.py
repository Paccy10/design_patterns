from .filter import Filter


class BlackAndWhiteFilter(Filter):

    def apply(self, file_name: str):
        print(f"Applying B&W filter to {file_name}")

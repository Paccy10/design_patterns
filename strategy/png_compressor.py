from .compressor import Compressor


class PNGCompressor(Compressor):

    def compress(self, file_name):
        print(f"Compressing {file_name} using PNG")

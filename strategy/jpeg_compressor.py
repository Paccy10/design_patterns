from .compressor import Compressor


class JPEGCompressor(Compressor):

    def compress(self, file_name):
        print(f"Compressing {file_name} using JPEG")

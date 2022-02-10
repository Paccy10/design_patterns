from strategy.black_and_white_filter import BlackAndWhiteFilter
from strategy.jpeg_compressor import JPEGCompressor


class ImageStorage:
    __compressor = None
    __filter = None

    def __init__(self, compressor: JPEGCompressor, filter: BlackAndWhiteFilter):
        self.__compressor = compressor
        self.__filter = filter

    def store(self, file_name: str):
        self.__compressor.compress(file_name)
        self.__filter.apply(file_name)

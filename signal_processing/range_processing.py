import numpy as np

class RangeProcessor:
    def __init__(self):
        pass

    def range_compress(self, raw_data):
        """
        Simulate matched filtering using FFT.
        Operates along range dimension.
        """
        compressed = np.fft.fft(raw_data, axis=1)
        return compressed


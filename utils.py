import time
import numpy


class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        self._start_time = time.perf_counter()

    def get_current_time(self):
        return time.perf_counter() - self._start_time

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return numpy.around(elapsed_time, 3)

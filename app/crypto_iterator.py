import time


class CryptoIterator:
    def __init__(self, data, interval=60):
        self.index = 0
        self.length = len(data)
        self.interval = interval

    def next(self):
        self.index += 1

        if self.index == self.length:
            self.index = 0

        time.sleep(self.interval)

    def get(self):
        return self.index

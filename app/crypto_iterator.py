import time
import json


class CryptoIterator:
    def __init__(self, interval=300):
        self.index = 0
        self.token_list = CryptoIterator.load()
        self.interval = interval

    @staticmethod
    def load():
        with open('./config.json') as reader:
            json_string = reader.read()
            json_data = json.loads(json_string)
            token_list = json_data["token_list"]

        return token_list

    def next(self):
        self.token_list = CryptoIterator.load()
        self.index += 1

        if self.index >= len(self.token_list):
            self.index = 0

        time.sleep(self.interval)

    def get(self):
        return self.token_list[self.index]

import srt
import random


class Subs:
    def __init__(self, filepath, encoding):
        subs_file = open(
            filepath,
            encoding=encoding,
        )
        self.subs = list(srt.parse(subs_file.read()))

    def get_random(self):
        return random.choice(self.subs)

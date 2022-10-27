from copy import deepcopy


class character:

    def __init__(self, char, colour):
        self.char = char
        self.color = colour


class guess:

    def __init__(self):
        self.char = []

    def append(self, value):
        self.char = self.char + [deepcopy(value)]
        return

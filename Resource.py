from random import *


class cpu(object):
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.moveset = []

    def batting(self, user):
        self.moveset = [choice(list(range(11))) for i in range(4 + self.difficulty)]
        if user in self.moveset:
            self.moveset.append(choice(list(range(11)).remove(user)))
        else:
            self.moveset.append(user)
        return_stuff = choice(self.moveset)
        self.moveset.clear()
        return return_stuff

    def bowling(self, user):
        self.moveset = [choice(list(range(11))) for i in range(7 - self.difficulty)]
        if user in self.moveset:
            self.moveset.append(choice(list(range(11)).remove(user)))
        else:
            self.moveset.append(user)
        return_stuff = choice(self.moveset)
        self.moveset.clear()
        return return_stuff




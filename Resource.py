from random import *
import Static_Resources


class Cpu(object):
    moves = list(range(11))

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.moveset = []

    def batting(self, user):
        self.moveset = Static_Resources.moveset_create_batting(user,self.difficulty)
        return_stuff = choice(self.moveset)
        self.moveset = self.moveset.clear()
        return return_stuff

    def bowling(self, user):
        self.moveset = Static_Resources.moveset_create_bowling(user, self.difficulty)
        return_stuff = choice(self.moveset)
        self.moveset = self.moveset.clear()
        return return_stuff



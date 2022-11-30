import random


class Player:

    def __init__(self, name, j):
        self.name = name
        self.speed = random.randint(2, 5)
        track = [j]
        for i in range(100):
            track.append("_")
        self.track = track

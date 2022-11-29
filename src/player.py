import random


class Player:

    def __init__(self, name):
        self.name = name
        self.speed = random.randint(2, 5)
        lane = []
        for _ in range(50):
            lane.append("_")
        self.track = lane

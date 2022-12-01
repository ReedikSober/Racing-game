
class Player:

    def __init__(self, name, j):
        self.name = name
        self.speed = 5
        track = [j]
        for _ in range(100):
            track.append("_")
        self.track = track

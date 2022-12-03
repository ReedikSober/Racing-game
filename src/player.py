
class Player:

    def __init__(self, name):
        self.name = name
        self.speed = 5
        track = [name[:2]]
        for _ in range(150):
            track.append("_")
        self.track = track

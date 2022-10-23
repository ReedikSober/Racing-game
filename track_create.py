

def track(xo, length):

    lane = list(xo)
    x = "_"

    for i in range(length * 12):
        lane.append(x)
    return lane

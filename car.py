
import random


class Car:
    def __init__(self, brand=0):

        self.brand = brand
        self.speed = random.randint(2, 5)

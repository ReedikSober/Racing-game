import time
from time import sleep
import random
import sys
import os
import csv
import operator
import colorama
from player import Player
from car import Car


def start_page():

    game_ended = False
    while not game_ended:
        os.system('cls||clear')
        print("==========WELCOME TO THE==========")
        print("===NEED FOR SPEED TERMINAL RACE===")
        print("1. Start Race")
        print("2. Scoreboard")
        print("3. Quit Game")
        print("Your choice: ")

        while True:
            try:
                main_menu = int(input(""))
                if main_menu in range(1, 4):
                    break
            except ValueError:
                print("Please select 1, 2 or 3")
            else:
                print("Please use a number from 1 to 3!")

        if main_menu == 1:
            main_logic()

        elif main_menu == 2:
            scoreboard()

        elif main_menu == 3:
            print("Thank you for playing")
            os.system('cls||clear')
            game_ended = True


def main_logic():

    player_1 = Player(input("Your name: "))
    print(f"Tell me more about yourself, {player_1.name}")
    player_car = Car(input("Your favourite car: "))

    while True:
        try:
            track_length = int(input("Track length: "))
            if track_length in range(1, 10):
                break
            else:
                print("Write a number from 1 to 9")
        except ValueError:
            print("Enter a number")

    round_ended = False
    while not round_ended:

        track_1 = track("X", track_length)
        track_2 = track("O", track_length)
        computer_car = Car()
        os.system('cls||clear')
        print("")
        print("=====START=====")
        print("")
        print(*track_1, sep='')
        print(*track_2, sep='')
        print("")

        c = 0
        z = 0

        turn_ended = False
        while not turn_ended:
            while True:
                start_time = time.time()

                while c < len(track_1) - 1 and z < len(track_2) - 1:

                    sys.stdout.write('\033[3A')

                    speed_player = range(random.randint(1, player_car.speed))
                    speed_player_max = speed_player[-1] + 1
                    for _ in speed_player:
                        track_1.insert(0, track_1.pop(len(track_1) - 1))
                    c = c + speed_player_max
                    print(*track_1, sep='')

                    speed_computer = range(random.randint(1, computer_car.speed))
                    speed_computer_max = speed_computer[-1] + 1
                    for _ in speed_computer:
                        track_2.insert(0, track_2.pop(len(track_2) - 1))
                    z = z + speed_computer_max
                    print(*track_2, sep='')
                    print("")
                    sleep(0.1)

                else:
                    print("=====FINISH=====")
                    print(f"{player_1.name}'s speed: {player_car.speed}")
                    print(f"Computer speed: {computer_car.speed}")
                    if c > z:
                        print(f"{player_1.name} WINS!")
                    elif z > c:
                        print("Computer WINS!")
                    elif c == z:
                        print("It's a TIE!")

                end_time = time.time()
                total_time = "%.3f" % (end_time - start_time)

                print(total_time)
                if c > z or c == z:
                    with open(f'scoreboard.csv', 'a') as f:
                        f.write(
                            f"Track {track_length}, {player_1.name} with {player_car.brand} going at "
                            f"{player_car.speed} lpi_______,{total_time}\n"
                        )
                break

            while True:
                another_round = input("Play another round? (y/n)")
                if another_round == "y":
                    turn_ended = True
                    break
                elif another_round == "n":
                    turn_ended = True
                    round_ended = True
                    break
                else:
                    print("Wrong option.")


def scoreboard():

    absolute_path = os.path.dirname(__file__)
    relative_path = "scoreboard.csv"
    full_path = os.path.join(absolute_path, relative_path)
    os.system('cls||clear')
    print("========== TOP PLAYERS ==========")

    data = csv.reader(
        open(full_path),
        delimiter=','
    )

    data = sorted(data, key=operator.itemgetter(0, 2))
    for i in data:
        print(*i, sep='')
    print("")
    print("What's next?")
    print("1. Return to main menu")
    print("2. Clear Scoreboard")
    print("")
    while True:
        try:
            user_input = int(input(""))
            if user_input in range(1, 3):
                break
        except ValueError:
            print("Please select 1 or 2")
        else:
            print("Please use a number from 1 to 2!")
    if user_input == 2:
        with open(f'scoreboard.csv', 'w'):
            print("Scoreboard is cleared!")
            sleep(2)


def track(xo, length):

    lane = list(xo)
    x = "_"

    for i in range(length * 12):
        lane.append(x)
    return lane


start_page()

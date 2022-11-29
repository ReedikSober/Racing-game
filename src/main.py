import time
from time import sleep
import random
import sys
import os
import csv
import operator
from src.player import Player


def start_page():
    os.system('cls||clear')
    print("==========WELCOME TO THE==========")
    print("===NEED FOR SPEED TERMINAL RACE===\n")
    print("1. Start Race")
    print("2. Scoreboard")
    print("3. Quit Game")

    while True:
        try:
            main_menu_select = int(input("\nYour choice: "))
            if main_menu_select in range(1, 4):
                break
        except ValueError:
            print("\nPlease select 1, 2 or 3")
        else:
            print("\nPlease use a number from 1 to 3!")

    user_options = {
        1: start_race,
        2: scoreboard,
        3: exit_game
    }

    user_options[main_menu_select]()


def create_player():
    global player
    player = [Player(input("Your name: ")) for i in range(3)]
    return player


def create_track():
    global track_length
    while True:
        try:
            track_length = int(input("Track length: "))
            if track_length in range(1, 10):
                break
            else:
                print("\nWrite a number from 1 to 9")
        except ValueError:
            print("\nEnter a number")

    return track_length


def exit_game():
    print("\nThank you for playing")
    sleep(2)
    os.system('cls||clear')
    exit()


def start_race():
    create_player()
    create_track()
    main_logic()


def game_engine():
    pass




def main_logic():
    track_1 = track("X", track_length)
    track_2 = track("O", track_length)
    computer_car = random.randint(2, 5)
    c = 0
    z = 0
    os.system('cls||clear')
    print("\n=====START=====\n")
    print(*track_1, sep='')
    print(*track_2, sep='')

    while True:
        start_time = time.time()
        while c < len(track_1) - 1 and z < len(track_2) - 1:

            sys.stdout.write('\033[4;0H')

            speed_player = range(random.randint(1,
                                                player.speed))  # make this a separate function, random function with seeds, user provides seeds
            speed_player_max = speed_player[-1] + 1
            for _ in speed_player:
                track_1.insert(0, track_1.pop(len(track_1) - 1))
            c = c + speed_player_max
            print(*track_1, sep='')

            speed_computer = range(random.randint(1, computer_car))
            speed_computer_max = speed_computer[-1] + 1
            for _ in speed_computer:
                track_2.insert(0, track_2.pop(len(track_2) - 1))
            z = z + speed_computer_max
            print(*track_2, sep='')
            sleep(0.07)

        else:
            print("\n=====FINISH=====\n")
            print(f"{player.name}'s speed: {player.speed}")
            print(f"Computer speed: {computer_car}\n")
            if c > z:
                print(f"{player.name} WINS!")
            elif z > c:
                print("Computer WINS!")
            elif c == z:
                print("It's a TIE!")

        end_time = time.time()
        total_time = "%.2f" % (end_time - start_time)

        print(f"With {total_time} seconds!")
        if c > z or c == z:
            with open(f'../scoreboard.csv', 'a') as f:
                f.write(
                    f"Track {track_length}, {player.name} going at {player.speed} lpi_______,{total_time} seconds\n"
                )
        break

    while True:
        another_round = input("\nPlay another round? (y/n)")
        if another_round == "y":
            main_logic()
        elif another_round == "n":
            start_page()
        else:
            print("Wrong option.")


def scoreboard():
    os.system('cls||clear')
    print("========== TOP PLAYERS ==========\n")

    data = csv.reader(
        open("../scoreboard.csv"),
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
            user_input = int(input())
            if user_input in range(1, 3):
                break
        except ValueError:
            print("Please select 1 or 2")
        else:
            print("Please use a number from 1 to 2!")
    if user_input == 2:
        with open(f'../scoreboard.csv', 'w'):
            print("\nScoreboard is cleared!")
            sleep(2)
            start_page()
    else:
        start_page()


def track(xo, length):
    lane = list(xo)
    x = "_"

    for _ in range(length * 12):
        lane.append(x)
    return lane


if __name__ == '__main__':
    start_page()

# multiplayer
# player provides a seed "do random"

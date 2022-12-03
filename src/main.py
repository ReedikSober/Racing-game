import time
from time import sleep
import random
import sys
import os
import csv
import operator
from player import Player

player = []
winner = []
total_time = None


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


def start_race():
    create_player()
    main_logic()


def create_player():
    global player
    number_of_players = 0
    player = []
    while True:
        try:
            number_of_players = int(input("Number of players: "))
        except ValueError:
            print("Please, enter a number")
            continue
        else:
            break
    for i in range(number_of_players):
        player.append(Player(input(f"Player {i + 1} name: ") or str(i + 1)))


def main_logic():
    global total_time
    os.system('cls||clear')
    print("\n=====START=====\n")

    start_time = time.time()
    game_engine()
    end_time = time.time()
    total_time = "%.2f" % (end_time - start_time)
    end_race()

    while True:
        another_round = input("\nPlay another round? (y/n): ")
        if another_round == "y":
            main_logic()
        elif another_round == "n":
            start_page()
        else:
            print("Wrong option.")


def game_engine():
    global winner
    finish = False
    winner = []
    while True:
        sys.stdout.write('\033[4;0H')
        for count, _ in enumerate(player):
            player_random_speed = random.randint(2, player[count].speed)
            position_1 = player[count].track.index(player[count].name[:2])
            position_2 = position_1 + player_random_speed
            player[count].track.pop(position_1)
            player[count].track.insert(position_2, player[count].name[:2])
            print(*player[count].track, sep='')
            if player[count].track[-1] == player[count].name[:2]:
                winner.append(player[count])
                finish = True
        if finish:
            return winner
        sleep(0.1)


def end_race():
    sys.stdout.write(f'\033[{len(player) + 6};0H')
    print("=====FINISH=====\n")
    for count, _ in enumerate(player):
        position_1 = player[count].track.index(player[count].name[:2])
        player[count].track.pop(position_1)
        player[count].track.insert(0, player[count].name[:2])

    for count, _ in enumerate(winner):
        print(f"{winner[count].name} WINS!")
        with open(f'../scoreboard.csv', 'a') as f:
            f.write(f"{winner[count].name} ___________________,{total_time} seconds\n")
    print(f"With {total_time} seconds!")


def scoreboard():
    j = 0
    os.system('cls||clear')
    print("========== TOP PLAYERS ==========\n")

    with open("../scoreboard.csv") as f:
        data = csv.reader(f, delimiter=',')
        data = sorted(data, key=operator.itemgetter(1))
    for i in data:
        j += 1
        print(*i, sep='')
        if j == 10:
            break

    print("\nWhat's next?")
    print("1. Return to main menu")
    print("2. Clear Scoreboard\n")

    while True:
        user_input = input("Your choice: ")
        if user_input == "1":
            start_page()
        elif user_input == "2":
            with open(f'../scoreboard.csv', 'w'):
                print("\nScoreboard is cleared!")
                sleep(2)
                start_page()
        else:
            print("Please select 1 or 2")


def exit_game():
    print("\nThank you for playing")
    sleep(2)
    os.system('cls||clear')
    exit()


if __name__ == '__main__':
    start_page()


# next update: Improve randomizer: player provides a seed "do random"
# use decorator to track time in main_logic()
# game class for track reset and creation, winner,
# data sorting before storing
# GUI

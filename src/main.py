import time
from time import sleep
import random
import sys
import os
import csv
import operator
from player import Player


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
    while True:
        try:
            number_of_players = int(input("Number of players: "))
        except ValueError:
            print("Please, enter a number")
            continue
        else:
            break
    j = 0
    player = []
    for i in range(number_of_players):
        j += 1
        player.append(Player(input(f"Player {j} name: ")))
    return player


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
        another_round = input("\nPlay another round? (y/n)")
        if another_round == "y":
            main_logic()
        elif another_round == "n":
            start_page()
        else:
            print("Wrong option.")


def game_engine():
    global winner
    j = -1

    while True:
        sys.stdout.write('\033[4;0H')
        for _ in player:
            j += 1
            player_random_speed = random.randint(1, player[j].speed)
            position_1 = player[j].track.index(player[j].name[:2])
            position_2 = position_1 + player_random_speed
            player[j].track.pop(position_1)
            player[j].track.insert(position_2, player[j].name[:2])
            print(*player[j].track, sep='')
            if player[j].track[-1] == player[j].name[:2]:
                winner = player[j]
                return winner

        sleep(0.1)
        j = -1


def end_race():
    j = -1
    sys.stdout.write(f'\033[{len(player) + 6};0H')
    print("=====FINISH=====\n")
    for _ in player:
        j += 1
        position_1 = player[j].track.index(player[j].name[:2])
        player[j].track.pop(position_1)
        player[j].track.insert(0, player[j].name[:2])
    print(f"{winner.name} WINS!")
    print(f"With {total_time} seconds!")
    with open(f'../scoreboard.csv', 'a') as f:
        f.write(f"{winner.name} ________________________,{total_time} seconds\n")


def scoreboard():
    os.system('cls||clear')
    print("========== TOP PLAYERS ==========\n")

    data = csv.reader(open("../scoreboard.csv"), delimiter=',')
    data = sorted(data, key=operator.itemgetter(1))

    for i in data:
        print(*i, sep='')
    print("\nWhat's next?")
    print("1. Return to main menu")
    print("2. Clear Scoreboard\n")

    while True:
        try:
            user_input = int(input("Your choice: "))
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


def exit_game():
    print("\nThank you for playing")
    sleep(2)
    os.system('cls||clear')
    exit()


if __name__ == '__main__':
    start_page()

# player provides a seed "do random"

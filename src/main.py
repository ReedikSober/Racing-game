import time
from dataclasses import dataclass
from time import sleep
from functools import wraps
import random
import sys
import os
import csv
from player import Player

player = []
winner = []
total_time = 0.00
absolute_path = os.path.dirname(__file__)
path_to_scoreboard = os.path.join(absolute_path, "scoreboard.csv")
with open(path_to_scoreboard, 'a'):
    pass


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        global total_time
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = float("%.2f" % (end_time - start_time))
        return result

    return timeit_wrapper


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
    os.system('cls||clear')
    print("\n=====START=====\n")

    game_engine()
    end_race()

    while True:
        another_round = input("\nPlay another round? (y/n): ")
        if another_round == "y":
            main_logic()
        elif another_round == "n":
            start_page()
        else:
            print("Wrong option.")


@timeit
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
                winner.append(Results(player[count].name))
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

    save_results()


def scoreboard():
    os.system('cls||clear')
    print("========== TOP PLAYERS ==========\n")

    show_result()

    print("\nWhat's next?")
    print("1. Return to main menu")
    print("2. Clear Scoreboard\n")

    while True:
        user_input = input("Your choice: ")
        if user_input == "1":
            start_page()
        elif user_input == "2":
            with open(path_to_scoreboard, 'w'):
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


@dataclass
class Results:
    name: str = "No Name"
    time: float = 0

    def list_out(self):
        return [self.time, self.name]


def show_result():
    with open(path_to_scoreboard, "r") as f:
        reader = csv.reader(f, delimiter=',')
        for count, line in enumerate(reader):
            res = Results(
                time=float(line[0]),
                name=str(line[1])
            )
            print(f"{count + 1}. {res.name} ________________ "
                  f"\033[{count + 3};21H {res.time} seconds")


def save_results():
    tmp = []
    with open(path_to_scoreboard, 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for count, line in enumerate(reader):
            res = Results(
                time=float(line[0]),
                name=str(line[1])
            )
            tmp.append(res)
            if count == 8:
                break
        for count, _ in enumerate(winner):
            new_res = Results(
                time=float(total_time),
                name=str(winner[count].name)
            )
            tmp.append(new_res)
            print(f"{winner[count].name} WINS!")
        print(f"With {total_time} seconds!")
        tmp.sort(key=lambda x: float(x.time))
    with open(path_to_scoreboard, 'w', newline="") as f2:
        writer = csv.writer(f2, delimiter=',')
        for res in tmp:
            out = res.list_out()
            writer.writerow(out)


if __name__ == '__main__':
    start_page()

# next update: Improve randomizer: player provides a seed "do random"
# game class for track reset and creation, winner,
# GUI

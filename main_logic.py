
def main_logic():
    import time
    from time import sleep
    import random
    import sys
    import colorama
    import os
    from track_create import track
    from player import Player
    from car import Car
    colorama.init()
    os.system("")

    player_1 = Player(input("Your name: "))
    player_1.printname()
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
                    for i in speed_player:
                        track_1.insert(0, track_1.pop(len(track_1) - 1))
                    c = c + speed_player_max
                    print(*track_1, sep='')
                    # sys.stdout.write("\r{0}>".format("="*i))


                    speed_computer = range(random.randint(1, computer_car.speed))
                    speed_computer_max = speed_computer[-1] + 1
                    for i in speed_computer:
                        track_2.insert(0, track_2.pop(len(track_2) - 1))
                    z = z + speed_computer_max
                    print(*track_2, sep='')
                    print("")
                    sleep(0.1)

                else:
                    print("=====FINISH=====")
                    print(f"Player car speer: {player_car.speed}")
                    print(f"Computer car speed: {computer_car.speed}")
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

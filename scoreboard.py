
import csv
import operator


def scoreboard():

    print("========== TOP PLAYERS ==========")

    data = csv.reader(
        open(
            'C:/Users/reedi/Desktop/SDA_Python_project'
            f'/lesson_6/car_race/scoreboard.csv'
        ),
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
    if user_input == 1:
        pass
    elif user_input == 2:
        with open(f'scoreboard.csv', 'w'):
            print("Scoreboard is cleared!")
            pass
        print("")

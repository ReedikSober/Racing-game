

def start_page():
    from main_logic import main_logic
    from scoreboard import scoreboard
    import os

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

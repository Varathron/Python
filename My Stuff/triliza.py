board = ["-","-","-","-","-","-","-","-","-"]
player = 1
game_not_ended = True
moves = 0
winner = None
place = 0
mark = ""
more_games = True

def display_board():

    print("\n" * 50)
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + "         " + "1 | 2 | 3")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + "         " + "4 | 5 | 6")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + "         " + "7 | 8 | 9")
    print("")


def play_game():

    display_board()

    while game_not_ended:
        turn()
        display_board()
        check_winner()
        check_tie()
        switch_player()

    print("Player " + str(winner) + " has won")


def turn():

    global board
    global place
    global mark
    global moves

    if player == 1:
        mark = "X"
    else:
        mark = "O"

    user_input()

    while board[place-1] != "-":
        display_board()
        print("This place is taken")
        user_input()

    place_mark_on_the_board()


def place_mark_on_the_board():

    global moves

    board[place - 1] = mark
    moves += 1


def user_input():

    global place

    place = int(input("Player " + str(player) + " using " + mark + " type your move: "))
    while place < 1 or place > 9:
        place = int(input("You must type a number between 1 and 9: "))


def check_winner():

    if check_rows() or check_columns() or check_diagonals():
        set_winner()


def set_winner():
    global winner
    global game_not_ended

    winner = player
    game_not_ended = False


def check_rows():

    if (board[0] == board[1] == board[2] and board[1] != "-" or
        board[3] == board[4] == board[5] and board[4] != "-" or
        board[6] == board[7] == board[8] and board[7] != "-"):
            return True


def check_columns():

    if (board[0] == board[3] == board[6] and board[3] != "-" or
        board[1] == board[4] == board[7] and board[4] != "-" or
        board[2] == board[5] == board[8] and board[5] != "-"):
            return True


def check_diagonals():

    if (board[0] == board[4] == board[8] and board[4] != "-" or
        board[6] == board[4] == board[2] and board[4] != "-"):
            return True


def check_tie():

    global game_not_ended

    if moves == 9 and winner == None:
        print("It's a tie")
        game_not_ended = False


def switch_player():

    global player

    if game_not_ended:
        if player == 1:
            player = 2
        else:
            player = 1


def board_initialize():

    global board
    global player
    global moves
    global winner
    global mark
    global game_not_ended

    board = ["-","-","-","-","-","-","-","-","-"]
    player = 1
    game_not_ended = True
    moves = 0
    winner = None
    place = 0
    mark = ""


def main_game_run():

    global more_games

    while more_games:
        play_game()

        more = raw_input("Play more? Y/N: ")
        while (more != "Y" and more != "N" and more != "y" and more != "n"):
            print("Type only Y or N")
            more = raw_input("Play more? Y/N: ")
        if more == "Y" or "y":
            board_initialize()

        if more == "N":
            more_games = False


main_game_run()

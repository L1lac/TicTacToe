#   Welcome to TicTacToe
#   This is a two player game where the players take turns in setting their symbol in 1 of the 9 availabe fields
#   Each player gets to choose the Symbol they want to use. Whoever gets to have 3 of his symbols in a row first, wins.
#   This is also the first code that I wrote completley on my own
#   I hope you enjoy!



import re

Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
turn = 1
win_condition = False
p1_condition = False
p2_condition = False
P1_symbol = "X"
P2_symbol = "O"


def print_Board():
    print(Board[0] + "|" + Board[1] + "|" + Board[2])
    print(Board[3] + "|" + Board[4] + "|" + Board[5])
    print(Board[6] + "|" + Board[7] + "|" + Board[8])


def p1_turn():
    global P1_symbol
    print_Board()

    user_input = input("\nP1, please choose where to place your symbol: ")

    try:
        index = Board.index(user_input)
        Board[index] = P1_symbol

    except ValueError:
        print("please choose an empty field.")
        p1_turn()


def p2_turn():
    global P2_symbol
    print_Board()

    user_input = input("\nP2, please choose where to place your symbol: ")

    try:
        index = Board.index(user_input)
        Board[index] = P2_symbol

    except ValueError:
        print("please choose an empty field.")

        p2_turn()


def p1_conditions():
    condition_1 = Board[0] == P1_symbol and Board[1] == P1_symbol and Board[2] == P1_symbol
    condition_2 = Board[3] == P1_symbol and Board[4] == P1_symbol and Board[5] == P1_symbol
    condition_3 = Board[6] == P1_symbol and Board[7] == P1_symbol and Board[8] == P1_symbol

    condition_4 = Board[0] == P1_symbol and Board[3] == P1_symbol and Board[6] == P1_symbol
    condition_5 = Board[1] == P1_symbol and Board[4] == P1_symbol and Board[7] == P1_symbol
    condition_6 = Board[2] == P1_symbol and Board[5] == P1_symbol and Board[8] == P1_symbol

    condition_7 = Board[0] == P1_symbol and Board[4] == P1_symbol and Board[8] == P1_symbol
    condition_8 = Board[6] == P1_symbol and Board[4] == P1_symbol and Board[2] == P1_symbol

    def winner():

        global p1_condition

        if condition_1:
            p1_condition = True

        elif condition_2:
            p1_condition = True

        elif condition_3:
            p1_condition = True

        elif condition_4:
            p1_condition = True

        elif condition_5:
            p1_condition = True

        elif condition_6:
            p1_condition = True

        elif condition_7:
            p1_condition = True

        elif condition_8:
            p1_condition = True

        else:
            p1_condition = False

    winner()


def p2_conditions():
    condition_1 = Board[0] == P2_symbol and Board[1] == P2_symbol and Board[2] == P2_symbol
    condition_2 = Board[3] == P2_symbol and Board[4] == P2_symbol and Board[5] == P2_symbol
    condition_3 = Board[6] == P2_symbol and Board[7] == P2_symbol and Board[8] == P2_symbol

    condition_4 = Board[0] == P2_symbol and Board[3] == P2_symbol and Board[6] == P2_symbol
    condition_5 = Board[1] == P2_symbol and Board[4] == P2_symbol and Board[7] == P2_symbol
    condition_6 = Board[2] == P2_symbol and Board[5] == P2_symbol and Board[8] == P2_symbol

    condition_7 = Board[0] == P2_symbol and Board[4] == P2_symbol and Board[8] == P2_symbol
    condition_8 = Board[6] == P2_symbol and Board[4] == P2_symbol and Board[2] == P2_symbol

    def winner():

        global p2_condition

        if condition_1:
            p2_condition = True

        elif condition_2:
            p2_condition = True

        elif condition_3:
            p2_condition = True

        elif condition_4:
            p2_condition = True

        elif condition_5:
            p2_condition = True

        elif condition_6:
            p2_condition = True

        elif condition_7:
            p2_condition = True

        elif condition_8:
            p2_condition = True

        else:
            p2_condition = False

    winner()


def check_win():
    global win_condition
    global turn

    if p1_condition:
        print_Board()
        print("\nP1 wins!")
        win_condition = True

    if p2_condition:
        print_Board()
        print("\nP2 wins!")
        win_condition = True

    if turn == 9 and p1_condition == False:
        print_Board()
        print("\nIt´s a draw!")
        win_condition = True


def game():
    global win_condition
    global Board
    global turn
    global p1_condition
    global p2_condition

    while not win_condition:
        p1_turn()
        p1_conditions()
        check_win()
        turn = turn + 1

        if turn >= 9:
            break
        elif p1_condition:
            break

        p2_turn()
        p2_conditions()
        check_win()
        turn = turn + 1

    if win_condition:

        game_restart = input("Do you want to play another round?\ny/n ")

        if game_restart == "y":
            win_condition = False
            Board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            p1_condition = False
            p2_condition = False
            turn = 1
            game()

        elif game_restart == "n":
            print("Thanks for playing!")
            
        else:
            print("Please input a valid option")

game()

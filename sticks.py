import re
import random


def sticks_gone(sticks):

    if sticks <= 0:
        return True
    else:
        return False



def game_loopAI():
    try:
            sticks = int(input("Select how many sticks you would like in the pile of sticks. \n Please enter a number between 10 and 100: "))
    except:
            print('You must enter a number')
            return game_loopAI()
    if sticks not in range(10, 101):
            print('You must enter a number 10 and 100.')
            return game_loopAI()

    while sticks_gone(sticks) == False:
        while sticks > 0:
            player1_sticks = input("Player 1: How many sticks would you like to take? (1-3) ")
            if player1_sticks not in ('1', '2', '3'):
                print("Can only pick up 1, 2 or 3 sticks.")
                continue
            if player1_sticks:
                player1_sticks = int(player1_sticks)
                if player1_sticks > sticks:
                    sticks -= player1_sticks

                else:
                    player1_sticks = player1_sticks
                    sticks -= player1_sticks
                    print('{} sticks remaining'.format(sticks))
            if sticks_gone(sticks) == True:
                x = input("You lost to the computer. Enter yes to play again: ")
                if x == 'yes':
                    return main()
                else:
                    exit()


            comp_sticks = random.randint(1, 3)
            print("The computer selected {}".format(comp_sticks))
            if comp_sticks:
                comp_sticks = int(comp_sticks)
                if comp_sticks > sticks:
                    sticks -= comp_sticks

                else:
                    comp_sticks = comp_sticks
                    sticks -= comp_sticks
                    print('{} sticks remaining'.format(sticks))
            if sticks_gone(sticks) == True:
                x = input("You beat the computer. Enter yes to play again: ")
                if x == 'yes':
                    return main()
                else:
                    exit()





def game_loop2():

    try:
            sticks = int(input("Select how many sticks you would like in the pile of sticks. \n Please enter a number between 10 and 100: "))
    except:
            print('You must enter a number')
            return game_loop2()
    if sticks not in range(10, 101):
            print('You must enter a number 10 and 100.')
            return game_loop2()

    while sticks_gone(sticks) == False:
        while sticks > 0:
            player1_sticks = input("Player 1: How many sticks would you like to take? (1-3) ")
            if player1_sticks not in ('1', '2', '3'):
                print("Can only pick up 1, 2 or 3 sticks.")
                continue
            if player1_sticks:
                player1_sticks = int(player1_sticks)
                if player1_sticks > sticks:
                    sticks -= player1_sticks

                else:
                    player1_sticks = player1_sticks
                    sticks -= player1_sticks
                    print('{} sticks remaining'.format(sticks))
            if sticks_gone(sticks) == True:
                x = input("Player 1, you lost. Enter yes to play again: ")
                if x == 'yes':
                    return main()
                else:
                    exit()


            player2_sticks = input("Player 2: How many sticks would you like to take? (1-3) ")
            if player2_sticks not in ('1', '2', '3'):
                print("Can only pick up 1, 2 or 3 sticks.")
                continue
            if player2_sticks:
                player2_sticks = int(player2_sticks)
                if player2_sticks > sticks:
                    sticks -= player2_sticks

                else:
                    player2_sticks = player2_sticks
                    sticks -= player2_sticks
                    print('{} sticks remaining'.format(sticks))
            if sticks_gone(sticks) == True:
                x = input("Player 2, you lost. Enter yes to play again: ")
                if x == 'yes':
                    return main()
                else:
                    exit()




def main():

    opponent = input("Would you like to play 1 player against the computer or 2 player? \n Enter '1' to play the computer or '2' for 2 player: " )
    if opponent == '1':
        game_loopAI()
    elif opponent == '2':
        game_loop2()
    else:
        return main()

# test






if __name__ == '__main__':
    main()

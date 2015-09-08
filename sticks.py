import re


def game_lopp(sticks):

    pass




def main():

    sticks = int(input("Please select how many sticks you would like in the pile of stinks. \n Please enter a number between 10 and 100: "))


    while True:
      while sticks > 0:
        player1_sticks = int(input("Player 1: How many sticks would you like to take? (1-3) "))
        if player1_sticks:
            sticks -= player1_sticks
            print('{} sticks remaining'.format(sticks))
        if sticks <= 0:
            x = input("Player 1, you lost. Enter yes to play again: ")
            if x == 'yes':
                return main()
            else:
                exit()
        player2_sticks = int(input("Player 2: How many sticks would you like to take? (1-3) "))
        if player2_sticks:
            sticks -= player2_sticks
            print('{} sticks remaining'.format(sticks))
        if sticks <= 0:
            x = input("Player 2, you lost. Enter yes to play again: ")
            if x == 'yes':
                return main()
            else:
                exit()



    # if sticks <= 0:
    #     x = input('Game over.  Enter yes to play again: ')
    #     if x == 'yes':
    #         return main()
    #     else:
    #         exit()




if __name__ == '__main__':
    main()

import re


def game_loop2():

    while True:
        sticks = int(input("Select how many sticks you would like in the pile of sticks. \n Please enter a number between 10 and 100: "))
        if sticks >= 10 and sticks <= 100:
            break
        else:
            print("Can only pick 10-100 sticks.")

    while True:
      while sticks > 0:
        player1_sticks = input("Player 1: How many sticks would you like to take? (1-3) ")
        if player1_sticks not in ('1', '2', '3'):
            print("Can only pick up 1, 2 or 3 sticks.")
            continue
        if player1_sticks:
            player1_sticks = int(player1_sticks)
            sticks -= player1_sticks
            print('{} sticks remaining'.format(sticks))

        if sticks <= 0:
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
            sticks -= player2_sticks
            print('{} sticks remaining'.format(sticks))

        if sticks <= 0:
            x = input("Player 2, you lost. Enter yes to play again: ")
            if x == 'yes':
                return main()
            else:
                exit()




def main():

    opponent = input("Would you like to play 1 player against the computer or 2 player? \n Enter '1' to play the computer or '2' for 2 player: " )
    if opponent == '1':
        print('ai')
    elif opponent == '2':
        game_loop2()
    else:
        return main()

# test






if __name__ == '__main__':
    main()

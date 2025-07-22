# start the game 
# ask the player to make a move (r, p, s)
# pc would select any move randmoly
# pc == player -> tie
# (player == p and pc == R) or (player == R and pc == s) or (player == s and pc == p)
## player won / you won 
# any other case 
## pc won / you lose 

import random
def start():
    while True:
        player = input("choose a move between ('r' for Rock , 'p' for Paper , 's' for scissors ) ")
        pc = random.choice (['r', 'p', 's'])


        if player == pc:
            print("It's a tie!")
        elif (player == 'p' and pc == 'r') or (player == 'r' and pc == 's') or (player == 's' and pc == 'p'):
            print("you won!")
        else:
            print("you lose!")

        print("User played  " + player )
        print("pc played    " + pc )
        wanna_play_again  = input(f"do you wanna play again? (yes/no) ").lower()
        if wanna_play_again == "no":
            print ("Thanks! ")
            break

start()
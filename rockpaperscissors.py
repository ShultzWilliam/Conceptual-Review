#rockpaperscissors.py - a simple console game where the user can input commands and play against a computer in Rock Paper Scissors
#the application keeps track of wins, losses, ties, and total games
#This game acts as a review on conditional statements in python
#Written by: William Shultz
#Initial Upload: January 12, 2022
#Last Updated: January 13, 2022

import random, sys

#Declare variables
wins, games, losses, ties = 0, 0, 0, 0

#introduction
print('welcome to Rock, Paper, Scissors')
print('the commands are r, p, s, q, h')


#while loop for game
while True:

    #displays current wins/losses/ties
    if games != 0:
        print("Total games:" + str(games) + "  Wins:" + str(wins) + "  Losses:" + str(losses) + "  Ties:" + str(ties))
    
    #wait for an input
    command = input(">>> ")

    #massive loop structure

    #quit command
    if command == 'q':
        print ("Shutting down...")
        sys.exit()
    
    #help command
    elif command == 'h':
        print("""The commands are as follows:
    r - rock
    p - paper
    s - scissors
    q - quit
    h - help""")
        continue

    #rock command
    elif command == 'r':
        print ('ROCK vs...')
    
    #paper command
    elif command == 'p':
        print('PAPER vs...')

    #scissor command    
    elif command == 's':
        print('SCISSORS vs...')

    #in case of invalid command
    else:
        print ('Please input a valid command.')
        continue

    #generate computer move
    randomNum = random.randint(1, 3)
    if (randomNum == 1):
        computer = 'r'
        print('ROCK')
    elif (randomNum == 2):
        computer = 'p'
        print('PAPER')
    else:
        computer = 's'
        print('SCISSORS')
    
    #tie cases
    if (command == 'r' and computer == 'r') or (command == 's' and computer == 's') or (command == 'p' and computer == 'p'):
        print('You tied!')
        ties += 1
    
    #win cases
    if (command == 'r' and computer == 's') or (command == 's' and computer == 'p') or (command == 'p' and computer == 'r'):
        print('You won!')
        wins += 1

    #loss cases
    if (command == 'r' and computer == 'p') or (command == 's' and computer == 'r') or (command == 'p' and computer == 's'):
        print('You lost...')
        losses += 1
    
    #keep track of games
    games += 1
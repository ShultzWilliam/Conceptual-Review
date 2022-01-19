#tictactoe.py
#This file is a 2-Player TicTacToe Game
#X and O take turns playing until one person wins or they tie.
#The file then ends whenever the controller inputs the endGame input
#Written by: William Shultz
#Initial Upload: January 19, 2022
#Last Updated: January 19, 2022

import random
import sys

#declaring global variables
#initial game state
board = {'TL':' ','TM':' ','TR':' ',
             'ML':' ','MM':' ','MR':' ',
             'BL':' ','BM':' ','BR':' '}
listOfStates = ['X','O']
moves = ["TL","TM",'TR','ML','MM','MR','BL','BM','BR']
xWins = 0
oWins = 0
ties = 0
totalGames = 0

#set all the board pieces back to default blank
def boardReset():
    for x in board:
        board[x]=' '

#reset moves list
def movesReset():
    global moves
    moves = ["TL","TM",'TR','ML','MM','MR','BL','BM','BR']

#function to print the board
def printBoard():
    print(board['TL'],"|",board['TM'],"|",board['TR'],sep='')
    print("-+-+-")
    print(board['ML'],"|",board['MM'],"|",board['MR'],sep='')
    print("-+-+-")
    print(board['BL'],"|",board['BM'],"|",board['BR'],sep='')

#determine gamestate
def startGameState():
    return random.choice(listOfStates)

#driver for a game
def newGame():
    #Reset the game state and give a random user the start
    boardReset()
    movesReset()
    gameState = startGameState()
    gameOver = False
    global xWins
    global oWins
    global ties
    global totalGames

    

    #Take turns until the game is over
    while gameOver == False:

        print("It's " + str(gameState) + "'s turn. ")
        printBoard()
        turn = input().upper()

        if turn not in moves:
            print("That's not a legal move. The legal moves are",moves)
            continue
        else:

            #Put the X or O where the player wants it
            board[turn]=gameState
            #that move is no longer available
            moves.remove(turn)
            printBoard()

            #check for winning states
            winningStates = ((board['TL'] == gameState and board['TM']==gameState and board['TR']==gameState) or
                (board['ML'] == gameState and board['MM']==gameState and board['MR']==gameState) or
                (board['BL'] == gameState and board['BM']==gameState and board['BR']==gameState) or
                (board['TL'] == gameState and board['ML']==gameState and board['BL']==gameState) or
                (board['TM'] == gameState and board['MM']==gameState and board['BM']==gameState) or
                (board['TR'] == gameState and board['MR']==gameState and board['BR']==gameState) or
                (board['TL'] == gameState and board['MM']==gameState and board['BR']==gameState) or
                (board['TR'] == gameState and board['MM']==gameState and board['BL']==gameState))

            #If someone made a winning move
            if (winningStates or len(moves)==0):
                gameOver = True
                break
            else:
                if gameState=='X':
                    gameState='O'
                else:
                    gameState='X'

    if winningStates:
        print("The winner is ",gameState,"!",sep='')
        if gameState == 'X':
            xWins += 1
        else: 
            oWins += 1

    else:
        print("It was a tie.")
        ties += 1
    totalGames +=1

    if totalGames != 0:
        print("X wins:",xWins,"   O wins:",oWins,"   ties:",ties,"   total games:")

#see what the player wants to do
def giveCommand():
    print("The commands are (P)lay and (Q)uit. What would you like to do?")
    command = input()
    command = command.upper()
    while command != 'P' and command != 'Q':
        print("please input a correct command.")
        command = input()
    if command == "P":
        newGame()
    else:
        print("Shutting down...")
        sys.exit()
    giveCommand()

#main function
print("Welcome to Tic-Tac-Toe!")
giveCommand()
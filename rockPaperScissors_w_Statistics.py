import random

total_Games_Played = 100
matchResults = []

print('Total games to be played: ' + str(total_Games_Played))

def rockPaperScissorsGame():
    
    player_One_Answer = ''
    player_Two_Answer = ''
    gameResult = ''

    choices = ['rock', 'paper', 'scissors']

    player_One_Answer = random.choice(choices)
    player_Two_Answer = random.choice(choices)

    #print('player one answer: ' + player_One_Answer)
    #print('player two answer: ' + player_Two_Answer)

    if player_One_Answer == player_Two_Answer:
        #print('game is a draw')
        gameResult = 'draw'
    elif player_One_Answer == 'rock' and player_Two_Answer == 'scissors':
        #print('player one wins')
        gameResult = 'win-1'
    elif player_One_Answer == 'paper' and player_Two_Answer == 'rock':
        #print('player one wins')
        gameResult = 'win-1'
    elif player_One_Answer == 'scissors' and player_Two_Answer == 'paper':
        #print('player one wins')
        gameResult = 'win-1'
    else:
        #print('player two wins')
        gameResult = 'win-2'

    return gameResult

def gettingMatchResults():
    for x in range(total_Games_Played):
        match_result = rockPaperScissorsGame()
        matchResults.append(match_result)

#print(matchResults)

def playerOneWins(matchResults):

    player_One_Wins = matchResults.count('win-1')
    
    return player_One_Wins

def playerTwoWins(matchResults):
    player_Two_Wins = matchResults.count('win-2')
    
    return player_Two_Wins

def totalDraws(matchResults):
    total_Drawn_Games = matchResults.count('draw')
    
    return total_Drawn_Games

gettingMatchResults()
print('Total drawn games: ' + str(totalDraws(matchResults)))
print('Total player 1 wins: ' + str(playerOneWins(matchResults)))
print('Total player 2 wins: ' + str(playerTwoWins(matchResults)))
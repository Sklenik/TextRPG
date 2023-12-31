import sys

# labels
introMessage = "Welcome brave adventurer!"  # TODO redo with pyfiglet ?

gameOverMessage = "GAME OVER"
victoryMessage = "You bravely fought various monsters of this land. Now the adventure has reached its end."

enemiesSlainMessage ="Total enemies slain: %d"
totalScoreMessage = "Total score: %d"

# functions
def intro():
    print(introMessage)

def gameOver(player, message):
    print('')
    print(gameOverMessage)
    print(message) # TODO custom death messages like ({PLAYERNAME} got crushed by {ENEMYNAME}) ? JSON ?
    scoreMessage(player)

def handleVictory(player):
    print('')
    print(victoryMessage)
    scoreMessage(player)

def scoreMessage(player):
    print(enemiesSlainMessage%player.enemiesSlain)
    print(totalScoreMessage%player.score)
    sys.exit()

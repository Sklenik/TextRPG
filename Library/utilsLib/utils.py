import sys
import random
import Library.jsonHelperLib.jsonHelper as jsonHelper

# TODO Clean up this mess, utils.py should not be so flooded

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
handlePlayerInputMessage = 'What do you wish to do? (Attack, Item, Magic, Random, Flee): '
repeatPlayerInputMessage = "Say, what was it again?"

playerAttackMessage = "You attacked for %d damage."
playerMissMessage = "You missed"

fleeQuestion = "Are you sure you want to flee? (y/n): "
fleeMessage = "%s has decided to quit adventuring for now."

enemiesSlainMessage ="Total enemies slain: %d"
totalScoreMessage = "Total score: %d"

enemyRetaliateMessage = "The %s got hit but refuses to give up and retaliates!"
enemyAttackMessage = "The %s attacks!"
enemyInflictsDamageMessage = "The %s inflicts %d points of damage."
playerKilledMessage = "You were slain by %s"
gameOverMessage = "GAME OVER" # TODO redo with pyfiglet ?
enemyMissedMessage = "The %s missed"
enemyKilled = "You have killed the %s !"

introMessage = "Welcome brave adventurer!"  # TODO redo with pyfiglet ?
enterContinueMessage = "Press enter to continue..."

# Handler functions
def handlePlayerInput(player, enemy):
    print(enemy.info())
    print(player)
    action = input(handlePlayerInputMessage)
    match action:
        case "Attack":
            handleAttack(player, enemy)
        case "Item":
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        case "Magic":
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        case "Random":
            print("Feature not implemented yet.")
            handlePlayerInput(player, enemy)
        case "Flee":
            handleFlee(player, enemy)
        # TODO add option pass ? So that with future over time effects like
        # poison or regeneration, the player can "skip turn"  or wait for
        # the enemy to die from effects instead of provoking it ?
        # TODO which leads to enemies being always hostile now, focus more on
        # the RPG aspect and enable finding and provoking enemies? stealth? KO ?
        # lot of work needs to be done it seems
        case _: # this means default case
            enterContinue(repeatPlayerInputMessage, True)
            handlePlayerInput(player, enemy)

    enterContinue('', False)
    handleEnemyAI(player, enemy)

def handleAttack(player, enemy):
    print('')
    playerDmg = player.calculateAttack()
    if playerDmg > 0:
        enemy.hit = True
        print(playerAttackMessage%playerDmg)
        enemy.hp -= playerDmg
        if enemy.hp <= 0:
            enemy.isDead = True
    else:
        print(playerMissMessage)

def handleItem(player, enemy): # TODO in version after handleMagic is finnisher
    # TODO make enemies drop collectable loot -> will there be an encumbrance or a backpack ? I dont know yet
    pass

def handleMagic(player, enemy): # TODO in next version
    pass

def handleRandom(player, enemy): # TODO in version after handleItem is finnished and tested
    pass

def handleFlee(player, enemy): 
    print('')
    action = input(fleeQuestion)
    if action == "y":
        print('')
        print(fleeMessage%player.name)
        handleScore(player)
    elif action == "n":
        handlePlayerInput(player, enemy)
    else:
        handleFlee(player, enemy)

def handleEnemyAI(player, enemy):
    if not enemy.isDead:
        if enemy.hit:
            enterContinue(enemyRetaliateMessage%enemy.type, True)
            enemy.hit = False
        else:
            enterContinue(enemyAttackMessage%enemy.type, True)
            
        enemyDmg = enemy.calculateAttack()
        if enemyDmg > 0:
            enterContinue(enemyInflictsDamageMessage%(enemy.type, enemyDmg), True)
            player.hp -= enemyDmg
            if player.hp <= 0:
                gameOver(player,playerKilledMessage%(enemy))
            else:
                handlePlayerInput(player, enemy)
        else:
            enterContinue(enemyMissedMessage%enemy.type, True)
            handlePlayerInput(player, enemy)
    else:
        sizes = jsonHelper.defaultSizes()
        player.score += 1 * 5 - sizes.index(enemy.size);
        player.enemiesSlain += 1
        enterContinue(enemyKilled%enemy, True)
        # this is where handleResult was in the early version. Now that it is
        # gone, the handleEnemyAI function ends, then the handlePlayerInput function
        # ends, and then the code continues in the game.py again

def handleVictory(player):
    print('')
    print("You bravely fought various monsters of this land. Now the adventure has reached its end.")
    handleScore(player)

def gameOver(player, message):
    print('')
    print(gameOverMessage)
    print(message) # TODO custom death messages like ({PLAYERNAME} got crushed by {ENEMYNAME}) ? JSON ?
    handleScore(player)

def handleScore(player):
    print(enemiesSlainMessage%player.enemiesSlain)
    print(totalScoreMessage%player.score)
    sys.exit()

# Selection functions
def selectRandom(group):
    position = random.randint(0,len(group)-1)
    return group[position]

# Console Output
def intro():
    print(introMessage)

def enterContinue(message, addspacebefore):
    if addspacebefore:
        print('')
    if message != '':
        print(message)
    return input(enterContinueMessage)
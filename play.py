import random
import json
import os
import sys

def clearScreen():
    os.system('cls')

# global variables
playerName = ""
size = ""
color = ""
creature = ""

playerhp = 10
enemyhp = 0
score = 0
enemiesSlain = 0

enemyHit = False
enemyKilled = False
dead = False


# select random var from list or array or whatever
def selectRandom(group):
    position = random.randint(0,len(group)-1)
    return group[position]

def createCreature(): # TODO overwork next time
    # Access enemies.json and parse it into an json object
    enemiesjson = open("C:/Users/fsklenar/Documents/personal code/Python/Game/Data/enemies.json",'r')
    enemies = json.load(enemiesjson)

    # Parse creature array into an array object
    creatures = enemies["creature"]

    global sizes
    sizes = ["tiny","small","big","huge","gargantuan"] # // TODO include this in JSON?
    sizes.reverse() # this is to fix the hp issue (for now)
    colors = ["red","orange","yellow","green","blue","purple","pink and pointy"] # // TODO include this in JSON?

    # choose random creature, size, color # TODO creature name ? other specification ?
    global creature # TODO it just works but I dont get how, this should probably be reworked to avoid future errors
    creature = selectRandom(creatures)
    global color
    color = selectRandom(colors)
    global size
    size = selectRandom(sizes)

    # calculate hp
    global enemyhp
    enemyhp = 5 - sizes.index(size)
    enemyhp *= random.randint(0,2)

def printOutEnemyHp():
    print("enemy hp: " + format(enemyhp))

def handlePlayerInput():
    print('')
    printHUD()
    #action = input('What do you wish to do? (Attack, Item, Magic, Random, Flee): ')
    action = input('What do you wish to do? (Attack, Magic, Flee): ')
    match action:
        case "Attack":
            handleAttack()
        case "Item": # TODO make enemies drop collectable loot -> will there be an encumbrance or a backpack ? I dont know yet
            print("Feature not implemented yet.")
            handlePlayerInput()
        case "Magic":
            handleMagic()
        case "Random":
            print("Feature not implemented yet.")
            handlePlayerInput()
        case "Flee":
            handleFlee()
        case _: # this means default case
            enterContinue("Say, what was it again?", True)
            handlePlayerInput()
    
    enterContinue('', False)
    handleEnemyAI()

def handleAttack():
    print('')
    playerdmg = random.randint(1,4) # TODO damage modifiers
    playerdmg *= random.randint(0,1) # TODO hit chance
    if playerdmg > 0:
        global enemyHit
        enemyHit = True
        print("You attacked for " + format(playerdmg) + " damage.")
        global enemyhp
        enemyhp -= playerdmg
        if enemyhp <= 0:
            global enemyKilled
            enemyKilled = True
            enemyHit = False
    else:
        print("You missed")

# TODO handleItem

def handleMagic():
    spells = ""
    options = []
    magicjson = open("C:/Users/fsklenar/Documents/personal code/Python/Game/Data/magic.json",'r')
    magic = json.load(magicjson)
    
    first = True
    for key in magic:
        spells += key
        options.append(key)
        if not first:
            spells += ", "
        else:
            first = False

    spellname = chooseSpell(spells, options)
    
    spell = magic[spellname]
    failChance = spell["failChance"]
    randInt = random.randint(0,failChance)
    if failChance == randInt:
        fails = spell["fails"]
        fail = selectRandom(fails)
        global playerhp
        if fail["damage"] > 0:
            print(fail["info"] + " (" + format(fail["damage"]) +" damage)")
            playerhp -= fail["damage"]
            if playerhp <= 0:
                gameOver(fail["deathMessage"])
        else:
            print(fail["info"])
    else:
        handleSpellEffects(spell)

def chooseSpell(spells, options): # FIXME returns none for some reason !!!!
    print('')
    action = input("Choose a spell (" + spells + "): ")
    if action in options:
        return action
        
    print("There is no such spell, choose again.")
    return chooseSpell(spells, options)

def handleSpellEffects(spell):        
    effects = spell["effects"]
    effect = selectRandom(effects)
    match spell["type"]:
        case "heal":
            global playerhp
            playerhp += effect["healValue"] # TODO maximum heal cap ?
            print(effect["info"] + "(heal " + format(effect["healValue"]) + ")")
        case _:
            exit("UNKNOWN TYPE") # TODO should I keep this here or make some process to load the JSONs before the game is launched?

        # TODO more types (weakness(nerf enemy abilities? will have duration?)?, hurt(instant, damage over time, damage that occurs at specific times? leech enemy health?)? spawn? text(say something that the enemy will react to(taunt, scare, offer, give, plead))? freeze(enemy doesnt attack freeze[time] times)?)

def handleFlee():
    print('')
    action = input("Are you sure you want to flee? (y/n): ")
    if action == "y":
        print('')
        print(playerName + " has decided to quit adventuring for now.")
        handleScore()
    elif action == "n":
        handlePlayerInput()
    else:
        handleFlee()

def handleEnemyAI():
    global enemyKilled
    if not enemyKilled:
        global enemyHit
        if enemyHit:
            enterContinue("The " + creature + " got hit but refuses to give up and retaliates!", True)
            enemyHit = False
        else:
            enterContinue("The " + creature + " attacks!", True)
            
        enemydmg = 5 - sizes.index(size)
        enemydmg *= random.randint(0,1)
        if enemydmg > 0:
            enterContinue("The " + creature + " inflicts " + format(enemydmg) + " points of damage.", True)
            global playerhp
            playerhp -= enemydmg
            if playerhp <= 0:
                gameOver("You were slain by " + size + ' ' + color + ' ' + creature)
            else:
                handlePlayerInput()
        else:
            enterContinue("The " + creature + " missed", True)
            handlePlayerInput()
    else:
        global score
        score += 1 * 5 - sizes.index(size);
        global enemiesSlain
        enemiesSlain += 1
        enemyKilled = False
        enterContinue("You have killed the " + size + ' ' + color + ' ' + creature + " !", True)
        handleResult()

def handleResult():
    print('')
    action = input("Do you wish to continue on your journey? (y/n): ") # TODO (y/n) action handler function ?
    if action == "y":
        loop()
    elif action == "n":
        handleVictory()
    else:
        handleResult()

def handleVictory():
    print('')
    print("You bravely fought various monsters of this land. Now the adventure has reached its end.")
    handleScore()

def gameOver(gameOverMessage):
    print('')
    print("GAME OVER")
    print(gameOverMessage) # TODO custom death messages ({PLAYERNAME} got crushed by {ENEMYNAME}) ? JSON ?
    handleScore()

def handleScore():
    print("Total enemies slain: " + format(enemiesSlain))
    print("Total score: " + format(score))
    sys.exit()
    
def loop(): # TODO not very nice? needs refactoring?
    createCreature() # XXX WARNING: IF THIS LINE IS OMMITED THEN THIS RESULTS IN INFINITE LOOP !!!
    print('')
    print("A " + size + ' ' + color + ' ' + creature + " appeared!")
    if enemyhp == 0:
        enterContinue("The " + creature + " instantly died because it was too weak.", False) # TODO custom death messages, make this very rare to happen as well
        loop()
    else:
        handlePlayerInput()

def game():
    # TODO later redo via classes ?
    # TODO difficulty - affect starting hp, hp cap, enemy hit chance, enemy hit damage, enemy bigger size chance, etc..
    
    print('') # TODO get rid of these prints ? Its flooding the code...
    print("Welcome brave adventurer!")
    global playerName
    playerName = input("How do you wish to be called? : ")
    enterContinue("A dangerous journey awaits!", False)
    loop()
    # TODO highscore? I guess top 10 players will do? - > JSON then print it out in a "table" (square of #) ?

def printHUD():
    printOutEnemyHp()
    playerInfo = "PLAYER:[" + playerName + "] HP:[" + format(playerhp) +"] SCORE:[" + format(score) + "]"
    print(playerInfo)

def enterContinue(message, addspacebefore):
    if addspacebefore:
        print('')
    if message != '':
        print(message)
    input("Press enter to continue...")

game()

# TODO github Git Repo? So that I dont lose progress and I can uncommit breaking changes ?

# TODO Fix the JSON file links ! Finished thing shouldn have the path to my user folder in it!
# TODO implement enemiesV2.json and overwork the enemy creation
# TODO bosses ?

# TODO make use of defaultColors.json and defaultLines.json
# TODO defaultLines.json -> use with placeholders (%X), when parsed, replace placeholders with values. %1 = size, %2 = color, %3 = creature, etc...
# TODO work more on the enemiesV2.json, more parameters? environments? environment lines, attacks and such?
# TODO maybe make simple enemiesV2 then create the Item system? (will need work on encumbrance/backpack system or something like that)
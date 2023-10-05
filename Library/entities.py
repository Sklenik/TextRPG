import random
from . import jsonHelper

# HUDs
playerHUD = "PLAYER:[%s] HP:[%d] SCORE:[%d]"
enemyInfoHUD = "Enemy Hp: [%d]"

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
backpackFullMessage = "The backpack is full. Do you wish to discard the item or replace existing? (discard, replace): "
discardAction = "discard"
replaceAction = "replace"
itemDiscardedMessage = "You decided to throw away the %s"
defaultSelectMessage = "Select an item: "
chooseItemToReplaceMessage = "Choose an item to replace: "
chooseItemToRemoveMessage = "Choose an item to remove: "

# player
class player():
    def __init__(self):
        self.entityType = ''
        self.name = ''
        self.hp = 0 # TODO affect with difficulty
        self.score = 0
        self.enemiesSlain = 0
        self.backpack = backpack(5) # TODO affect with encumbrance ? Add with player skills/exp/levels update?

    def __str__(self):
        playerInfo = playerHUD%(self.name, self.hp, self.score)
        return playerInfo
    
    def calculateAttack(self):
        playerDmg = random.randint(1,4) # TODO damage modifiers
        playerDmg *= random.randint(0,2) # TODO hit chance
        return playerDmg

# Enemy
class enemy():
    def __init__(self, entityType):
        self.entityType = entityType
        self.size = ''
        self.color = ''
        self.type = ''
        self.hp = 0
        self.hit = False
        self.isDead = False
        assignEnemySpecification(self)
        assignEntityHp(self)
        self.loot = backpack(3) # TODO next time implement the drop system on enemy death + randomize backack size and loot + implement creaturesV2 !

    def __str__(self):
        if self.size != '':
            return f"{self.size} {self.color} {self.type}"
        return f"{self.color} {self.type}"
    
    def info(self):
        enemyInfo = enemyInfoHUD%self.hp
        return enemyInfo
    
    def calculateAttack(self):
        sizes = jsonHelper.getSizes()
        sizes.reverse()
        enemyDmg = 6 - sizes.index(self.size) # TODO damage modifiers
        enemyDmg *= random.randint(0,2) # TODO hit chance
        return enemyDmg

def assignEnemySpecification(entity):
    match entity.entityType:
        case "creature":
            jsonHelper.initCreatureSpecificationV1(entity)

def assignEntityHp(entity):
    sizes = jsonHelper.getSizes()
    sizes.reverse()
    # TODO maybe make sizes in the JSON as json objects, containing hp info?
    entity.hp = len(sizes) - sizes.index(entity.size)

# Creature
def createCreature(): # TODO create diferent enemies, not just creatures ?
    creature = enemy("creature")
    return creature


# Backpack
class backpack():
    def __init__(self, defaultSlots):
        self.defaultSlots = defaultSlots # TODO this will be affected by future processes later? like player encumbrance?
        self.items = []
        self.skin = ""
        self.slotSkin = ""
        self.nullSkin = ""
        jsonHelper.initDefaultBackpack(self)

    def __str__(self):
        return createRectangleV2(self)
    
    def nullCount(self):
        return self.items.count(self.nullSkin)

    def addItem(self, newItem):
        if self.nullCount() == 0:
            backpackFull(self, newItem)
        else:
            indx = self.items.index(self.nullSkin)
            self.items[indx] = newItem

    def selectItem(self, selectMessage=defaultSelectMessage):
        print(self)
        item = input(selectMessage)
        if (item in self.items) and (item != self.nullSkin):
            return item
        else:
            return self.selectItem(selectMessage)
        
    def replaceItem(self, itemToReplace, newItem='', dialog=False):
        if dialog:
            itemToReplace = self.selectItem(chooseItemToReplaceMessage)
        indx = self.items.index(itemToReplace)
        if newItem == '':
            self.items[indx] = self.nullSkin
        else:
            self.items[indx] = newItem

    def removeItem(self, itemToDelete, dialog=False):
        if dialog:
            itemToDelete = self.selectItem(chooseItemToRemoveMessage)
        self.replaceItem(itemToDelete)

def formatBackpackList(bag):
    formatedList = []
    
    for item in bag.items:
        if item == bag.nullSkin:
            formatedList.append(item)
        else:
            formatedList.append(bag.slotSkin%item)
    
    return formatedList
        
def getLengthOfLongestWord(list):
    length = 0
    for word in list:
        if len(word) > length:
            length = len(word)
    return length    

def createRectangleV2(bag):
    formatedList = formatBackpackList(bag)
    mainLen = getLengthOfLongestWord(formatedList)

    skin = bag.skin

    FullRow = 2*skin + mainLen*skin + 2*skin
    RowLen = len(FullRow)
    
    rectangle = FullRow + "\n"

    for item in formatedList:
        base = skin + ' ' + item
        noOfSpaces = RowLen - len(base) - 1
        wordRow = base + noOfSpaces*' ' + skin
        rectangle += wordRow + "\n"

    rectangle += FullRow
    return rectangle

def backpackFull(bag, newItem):
    action = input(backpackFullMessage)
    if action == discardAction:
        print(itemDiscardedMessage%newItem)
    elif action == replaceAction:
        bag.replaceItem('', newItem, True)

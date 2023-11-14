import random
from . import utils, jsonHelper
from .handlers import messageHandlers

# HUDs
playerHUD = "PLAYER:[%s] HP:[%d] SCORE:[%d]"
enemyInfoHUD = "Enemy Hp: [%d]"

# Labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vrrs to create translations ?
backpackFullMessage = "The backpack is full. Do you wish to discard the item(%s) or replace existing? (discard, replace): "
backpackEmptyMessage = "The backpack is empty."
discardAction = "discard"
replaceAction = "replace"
itemDiscardedMessage = "You decided to throw away the %s"
defaultSelectMessage = "Select an item: "
chooseItemToReplaceMessage = "Choose an item to replace: "
chooseItemToRemoveMessage = "Choose an item to remove: "

# Errors
itemNotStackableError = 'ERROR - item not stackable'

# player
class player():
    def __init__(self, bagslots=5):
        self.entityType = ''
        self.name = ''
        self.hp = 0 # TODO affect with difficulty
        self.score = 0
        self.enemiesSlain = 0
        self.backpack = backpack(bagslots) # TODO affect with encumbrance ? Add with player skills/exp/levels update?

    def __str__(self):
        playerInfo = playerHUD%(self.name, self.hp, self.score)
        return playerInfo
    
    def calculateAttack(self):
        playerDmg = random.randint(1,4) # TODO damage modifiers
        playerDmg *= random.randint(0,2) # TODO hit chance
        return playerDmg

# Enemy
class enemy():
    def __init__(self, entityType='', bagslots=3):
        self.entityType = entityType
        self.size = ''
        self.color = ''
        self.name = ''
        self.rarity = ''
        self.hp = 0
        self.hit = False
        self.isDead = False
        self.loot = backpack(bagslots)
        initEnemyValues(self)
        assignEntityHp(self)

    def __str__(self):
        if self.size != '':
            return f"{self.size} {self.color} {self.name}"
        return f"{self.color} {self.name}"
    
    def info(self):
        enemyInfo = enemyInfoHUD%self.hp
        return enemyInfo
    
    def calculateAttack(self):
        sizes = jsonHelper.getSizes()
        sizes.reverse()
        enemyDmg = 6 - sizes.index(self.size) # TODO damage modifiers
        enemyDmg *= random.randint(0,2) # TODO hit chance
        return enemyDmg
    
    def enemyDead(self, player):
        pass # TODO enemy drop system

def initEnemyValues(entity):
    match entity.entityType:
        case "creature":
            jsonHelper.initCreatureSpecificationV2(entity)
            jsonHelper.initCreatureLootV2(entity)

def assignEntityHp(entity):
    sizes = jsonHelper.getSizes()
    sizes.reverse()
    # TODO maybe make sizes in the JSON as json objects, containing hp info?
    entity.hp = len(sizes) - sizes.index(entity.size)

# Creature
def createCreature(): # TODO create diferent enemies, not just creatures ?
    creature = enemy("creature")
    return creature 

# Item
class item():
    def __init__(self, type='', rarity='', name='', count=1, stackable=True, skin="<%s>[%s]{%d}"):
        self.type = type #TODO move into some function, json or something? Some "enum-like" class maybe ?
        self.rarity = rarity
        self.name = name
        self.stackable = stackable
        self.count = count
        self.skin = skin
        #TODO weight (for the encumbrance system)?
        
        # type specific
        self.healValue = 0 

    def __str__(self):
        return self.skin%(self.rarity, self.name, self.count)
    
    def checkStackable(self):
        if not self.stackable:
            messageHandlers.error(itemNotStackableError)
    
    def add(self, count):
        self.checkStackable()
        self.count += count
        return True
    
def nullItem():
    null = item()
    return null

# Backpack
class backpack():
    def __init__(self, defaultSlots=5):
        self.defaultSlots = defaultSlots # TODO this will be affected by future processes later? like player encumbrance?
        self.items = []
        self.skin = ""
        self.slotSkin = ""
        self.nullSkin = ""
        jsonHelper.initDefaultBackpack(self) # TODO change this to implement skins

    def __str__(self):
        return createRectangle(self)
    
    def nullCount(self):
        return formatItems(self).count(self.nullSkin)
    
    def getItemByName(self, name):
        for item in self.items:
            if item.name == name:
                return item
        return nullItem()
    
    def addItem(self, newItem):
        existingItem = self.getItemByName(newItem.name)
        if existingItem.name != '':
            existingItem.add(newItem.count) # TODO later when weight is implemented, this will have to be reworked slightly
        else:
            if self.nullCount() == 0:
                backpackFull(self, newItem)
            else:
                indx = formatItems(self).index(self.nullSkin)
                self.items[indx] = newItem

    def selectItem(self, selectMessage=defaultSelectMessage):
        print(self)
        name = input(selectMessage)
        item = self.getItemByName(name)
        return item
        
    def replaceItem(self, itemToReplace, newItem=nullItem(), dialog=False): # TODO item will have to be either class or dictionary for this to work properly, I'm not in the mood to fix it rn
        if dialog:
            itemToReplace = self.selectItem(chooseItemToReplaceMessage)

        if itemToReplace.name == '':
            self.replaceItem(itemToReplace, newItem, True)
        else:
            indx = formatItems(self).index(format(itemToReplace))
            if newItem.name == '':
                self.items[indx] = nullItem()
            else:
                self.items[indx] = newItem

    def removeItem(self, dialog=True, itemToDelete=nullItem()):
        if dialog:
            itemToDelete = self.selectItem(chooseItemToRemoveMessage)
        self.replaceItem(itemToDelete)
    
    def substractItem(self, itemToSubstract, count=1) -> int: # returns remaining quantity of the item
        itemToSubstract.count -= count
        if itemToSubstract.count <= 0:
            self.removeItem(False, itemToSubstract)
            return 0
        return count

    def IsEmpty(self):
        return self.nullCount() == self.defaultSlots

    def checkIsEmpty(self):
        if not self.IsEmpty():
            return False
        print(backpackEmptyMessage)
        return True
            
def formatItems(bag):
    formatedList = []
    for item in bag.items:
        if item.name == '':
            formatedList.append(bag.nullSkin)
        else:
            formatedList.append(format(item))
    return formatedList

def getLengthOfLongestItem(list):
    length = 0
    for item in list:
        if len(format(item)) > length:
            length = len(format(item))
    return length

def getLengthOfLongestWord(list):
    length = 0
    for word in list:
        if len(word) > length:
            length = len(word)
    return length
  
def createRectangle(bag):
    # mainLen = getLengthOfLongestItem(bag.items)
    formatedList = []
    formatedList = formatItems(bag)
    mainLen = getLengthOfLongestWord(formatedList)

    skin = bag.skin

    FullRow = 2*skin + mainLen*skin + 2*skin
    RowLen = len(FullRow)
    
    rectangle = FullRow + "\n"

    for string in formatedList:
        base = skin + ' ' + string
        noOfSpaces = RowLen - len(base) - 1
        wordRow = base + noOfSpaces*' ' + skin
        rectangle += wordRow + "\n"

    rectangle += FullRow
    return rectangle

def backpackFull(bag, newItem, showBag=True):
    if showBag:
        print(bag)

    action = input(backpackFullMessage%(newItem))
    if action == discardAction:
        print(itemDiscardedMessage%newItem.name)
    elif action == replaceAction:
        print('')
        bag.replaceItem('', newItem, True)
    else:
        print('')
        backpackFull(bag, newItem)

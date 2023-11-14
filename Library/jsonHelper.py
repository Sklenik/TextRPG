import json
from . import utils, entities
path = "Data/JSON/"

# default.json procedures
def getSizes():
    file = open(path + "default.json", 'r')
    default = json.load(file)
    sizes = default["sizes"]
    return sizes

def getColors():
    file = open(path + "default.json", 'r')
    default = json.load(file)
    colors = default["colors"]
    return colors

# creature procedures
def creatureList():
    file = open(path + "enemies.json", 'r')
    enemies = json.load(file)
    creatures = enemies["creatures"]
    return creatures

def initCreatureSpecificationV2(creatureClass):
    creatureClass.size = utils.selectRandom(getSizes())
    creatureClass.color = utils.selectRandom(getColors())
    keyAndValue = utils.selectRandomKeyAndValue(creatureList())
    creatureClass.name = keyAndValue[0]

def initCreatureLootV2(creatureClass):
    creatures = creatureList()
    creature = creatures[creatureClass.name]
    creatureClass.loot.defaultSlots = creature["bagSize"]

    for i in range(creatureClass.loot.defaultSlots):
        rarity = utils.selectRandom(creature["rarity"])
        
        consumablesByRarityList = getConsumablesByRarity(rarity)
        consumables = consumablesByRarityList[1]
        randomConsumable = utils.selectRandomKeyAndValue(consumables)

        item = entities.item("consumable", # TODO add other item types when impemented, maybe add section to enemies.json where item types are specified?
                             rarity,
                             randomConsumable[0], # consumable name
                             1, # TODO maybe add more than one ? based on what tho ?
                             True) # TODO test properly
        item.healValue = randomConsumable[1]

        creatureClass.loot.addItem(item)

# magic procedures
def getMagic():
    file = open(path + "magic.json",'r')
    magic = json.load(file)
    return magic

# backpack procedures
def initDefaultBackpack(backpack):
    file = open(path + "backpack.json",'r')
    skins = json.load(file)
    skin = skins["default"]

    backpack.skin = skin["backpackSkin"]
    backpack.slotSkin = skin["slotSkin"]
    backpack.nullSkin = skin["nullSkin"]

    for i in range(backpack.defaultSlots):
        backpack.items.append(entities.nullItem())

# item procedures
def getConsumables(): # TODO improve? implement fail system (rotten/poisoned/cursed items)?
    file = open(path + "items/consumables.json")
    # TODO Add mysterious soup - item with random properties -> can damage the player
    consumables = json.load(file)
    return consumables

def getConsumablesByRarity(rarity='') -> list:
    if rarity == '':
        rarity = utils.getRarity()

    jsonFile = getConsumables()
    consumables = jsonFile[rarity]
    return [rarity, consumables]

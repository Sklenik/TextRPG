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

def initCreatureSpecificationV1(creatureClass):
    creatureClass.size = utils.selectRandom(getSizes())
    creatureClass.color = utils.selectRandom(getColors())
    creatureClass.type = utils.selectRandom(creatureList())

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

# item procedures # TODO needs rework ?
def getConsumables():
    file = open(path + "items/consumables.json")
    consumables = json.load(file)
    return consumables
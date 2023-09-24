import json
from Library import utils
path = "./Data/JSON/"

# default.json procedures
def defaultSizes():
    file = open(path + "default.json")
    default = json.load(file)
    sizes = default["sizes"]
    return sizes

def defaultColors():
    file = open(path + "default.json")
    default = json.load(file)
    colors = default["colors"]
    return colors

# Creature procedures
def creatureList():
    file = open(path + "enemies.json")
    enemies = json.load(file)
    creatures = enemies["creatures"]
    return creatures

def initCreatureSpecificationV1(creatureClass):
    creatureClass.size = utils.selectRandom(defaultSizes())
    creatureClass.color = utils.selectRandom(defaultColors())
    creatureClass.type = utils.selectRandom(creatureList())

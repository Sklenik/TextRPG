import random
import Library.jsonHelperLib.jsonHelper as jsonHelper

# HUDs
playerHUD = "PLAYER:[%s] HP:[%d] SCORE:[%d]"
enemyInfoHUD = "Enemy Hp: [%d]"

# player
class player():
    def __init__(self):
        self.entityType = ''
        self.name = ''
        self.hp = 0 # TODO affect with difficulty
        self.score = 0
        self.enemiesSlain = 0

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

    def __str__(self):
        if self.size != '':
            return f"{self.size} {self.color} {self.type}"
        return f"{self.color} {self.type}"
    
    def info(self):
        enemyInfo = enemyInfoHUD%self.hp
        return enemyInfo
    
    def calculateAttack(self):
        sizes = jsonHelper.defaultSizes()
        sizes.reverse()
        enemyDmg = 6 - sizes.index(self.size) # TODO damage modifiers
        enemyDmg *= random.randint(0,2) # TODO hit chance
        return enemyDmg

def assignEnemySpecification(entity):
    # TODO maybe throw away the entityTypes ? don't know what that's useful for right now...
    match entity.entityType:
        case "creature":
            jsonHelper.initCreatureSpecificationV1(entity)

def assignEntityHp(entity):
    sizes = jsonHelper.defaultSizes();
    sizes.reverse()
    # TODO maybe make sizes in the JSON as json objects, containing hp info?
    entity.hp = len(sizes) - sizes.index(entity.size) #FIXME object of type nonetype has no len

# Creature
def createCreature():
    creature = enemy("creature")
    return creature

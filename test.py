# This file serves only for testing the latest changes. Do not merge into master
from Library import entities
from Library import utils

player = entities.player("",0)

def Play():
    utils.intro()
    player.name = input("How do you wish to be called? : ")
    player.hp = 10
    utils.enterContinue("A dangerous journey awaits!", False)
Play()
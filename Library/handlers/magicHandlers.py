import random
from .. import jsonHelper, utils
from . import messageHandlers

# labels
# TODO use these vars to provide different versions of the messages later, using data saved in something like lines.json
# TODO use these vars to create translations ?
chooseSpellMessage = "Choose a spell (%s): "
failMessage = "%s (%d damage)"
healMessage = "%s (heal %d)"

# functions
def handleMagic(player, enemy):
    magic = jsonHelper.getMagic()

    spells = []
    spellsTxt = ""
    
    first = True
    for key in magic:
        spells.append(key)
        spellsTxt += key
        if not first:
            spells += ", "
        else:
            first = False

    spellName = chooseSpell(spellsTxt, spells)
    spell = magic[spellName]

    if not utils.failHandler(spell["fails"], spell["failChance"], failMessage, player):
        handleSpellEffects(player, enemy, spell)

def chooseSpell(spellsTxt, spells):
    print()
    spell = input(chooseSpellMessage%spellsTxt)
    if spell in spells:
        return spell
    return chooseSpell(spellsTxt, spells)

def handleSpellEffects(player, enemy, spell):        
    effects = spell["effects"]
    effect = utils.selectRandom(effects)
    match spell["type"]:
        case "heal":
            player.hp += effect["healValue"] # TODO maximum heal cap ?
            print(healMessage%(effect["info"], effect["healValue"]))
        case _:
            exit("UNKNOWN TYPE") # TODO should I keep this here or make some process to load the JSONs before the game is launched?

        # TODO more types (weakness(nerf enemy abilities? will have duration?)?, hurt(instant, damage over time, damage that occurs at specific times? leech enemy health?)? spawn? text(say something that the enemy will react to(taunt, scare, offer, give, plead))? freeze(enemy doesnt attack freeze[time] times)?
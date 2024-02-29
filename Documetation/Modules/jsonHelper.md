# jsonHelper.py

## Functions

### getSizes

Parses default sizes into a list and returns it.

### getColors

Parses default colors into a list and returns it.

### creatureList

Parses creatures into a dictionary and returns it.

### initCreatureSpecificationV2

Enemy class is passed to the function.

The class gets a random size and color. Then it selects a random name from the creatures list.

### initCreatureLootV2

Enemy class of type Creature is passed to the function.

The function finds detail about the creature. Then assigns the bagsize to the creature.

Then for each empty slot an item is added to the creature loot. It can happen that one or more slots will remain empty, as some items can stack. The count of the items added equals the count of the creature loot slots.

### getMagic

Parses the magic.json inot a dictionary and returns it.

### initDefaultBackpack

Parses data from backpack.json into a provided backpack class (passed as parameter). This means the backpack gets its visual appearance assigned.

Then the empty slots are added to the backpack. The count of empty slots equals the backpack.defaultSlots property.

### getConsumables

Parses the consumables.json into a dictionary and returns it.

### getConsumablesByRarity

Rarity is passed as a parameter to the function. The function then parses only the consumables of the provided rarity and returns them in a list. The list format is \[RARITY, CONSUMABLES=\[CONSUMABLE,...]].
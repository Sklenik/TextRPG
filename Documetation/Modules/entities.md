# entities.py

## classes

### player
This is the class that creates the player object which is then passed throughout the entire game loop.

Parameters
 - entity type - this indicates that the class is a player, this will possibly become useless in the future versions
 - bagslots - defines player inventory size

This class stores:
 - player name
 - player hp
 - player score
 - count of enemies slain by the player
 - player inventory - this uses the [backpack](#backpack) class

Built-in functions
 - When printed, the class displays *"PLAYER:[\string] HP:[\float] SCORE:[\float]"*. This is considered the "HUD" and it's currently hardcoded.
 - *calculateAttack* that's used to calculate the player attack dmg.

### enemy
This is the class that creates the enemy object which is then passed throughout the entire game loop.

Parameters
 - Entity type - has an importance here, as it states which enemy type is to be created and then it indicates the type to the game loop. Currently the game has only one type of enemy - *creature*. However, this is about to change in future updates.
 - bagslots - defines enemy inventory size

This class stores:
 - size - size of the enemy, both cosmetic and funcitonal value. Used to calculate enemy HP when enemy is created and is also used when enemy is printed out.
 - color - displayed in the HUD, randomly generated
 - name - displayed in the HUD, randomly generated
 - rarity - assigned from the enemies json, each enemy has predefined rarities. Rarity gets picked from the predefined list. Rarity also influences the enemy loot.
 - hp - calculated from the size
 - hit - indicates whether the enemy has been damaged at least once by the player
 - isDead - indicates whether the enemy has been killed by the action
 - loot - this uses the [backpack](#backpack) class. Generated using the rarity and bagslots

Built-in funcitons
 - when printed and size is not '', displays size, color, name. If size is '', displays color, name
 - *info* - displays *"string - HP:[\float]"* where the string is the enemy name and the float indicates the HP
 - *calculateAttack* - calculates attack using sizes

Related functions
 - *initEnemyValues* - assigns name, rarity, size and loot of the enemy, using the jsonHelper functions
 - *assignEntityHp* - calculates the enemy HP using sizes
 - *createCreature* - create an enemy of type creature (assigns entityType and initializes the enemy class)

How does the player HUD look in the console\
![playerHud](/Data/Static/playerHud.png)

### item
This is the class that creates the itenm object which is passed to [backpack](#backpack) class and used to keep track of individual item data.

Parameters
 - type
   - *consumable* - item that heals when consumed
   - planed types: *armour, artifacts, potions, weapons*.
 - rarity
   - influences the healvalue of consumables
 - name - name of the item
 - count - if stackable, defines the current amount in the stack
 - stackable - defines if item can be stacked
 - skin - how item looks when printed
 - noQtySkin - how item looks when printed without qty

This class stores:
 - type
 - rarity
 - name
 - count
 - stackable
 - skin - "<%s>[%s]{%d}" - rarity, name, count
 - noQtySkin - "<%s>[%s]" - rarity, name
 - healValue - how much hp does an item heal if consumed

Built-in functions
 - *noQtyName* - returns name without qty using the noQtySkin
 - *checkStackable* - throws an error if item isn't stackable
 - *add* - increments the count of the item stack, if stackable

Related functions
 - *nullItem* - creates null item used to create empty [backpack](#backpack) slots

How does the enemy HUD look in the console\
![enemyHud](/Data/Static/enemyHud.png)

### backpack
This is the class that creates backpack itenm object which is passed to player and enemy classess, used to keep track of entity inventory. Stores and manages item classes.

Parameters
 - defaultSlots - defines the backpack size, i.e. the amount of stacks the backpack can store

This class stores
 - items - list of item classes
 - skin - backpack skin used for the backpack sides when it's printed out
 - slotSkin - how a stack looks in the bag
 - nullSkin - how an empty stack looks in the bag

Built-in functions
 - *nullCount* - returns the count of empty stacks, i.e. available backpack space
 - *getItemByName* - gets item stack by it's name. This will be replaced with some kind of ID in the future, to keep track of duplicit item stacks.
 - *addItem* - adds item to the backpack or increments the count of the item in existin stack. Has some logic programmed to make the player discard items if the backpack is full and can no longer be filled.
 - *selectItem* - interface for player to select an item in the bag for related processes like consuming the item
 - *replaceItem* - replace selected item stack with another stack and discard the replaced stack
 - *removeItem* - remove selected item stack
 - *substractItem* - decrements items from stack. Removes the stack if 0 qty is reached.
 - *isEmpty* - returns true if backpack only contains null items
 - *checkIsEmpty* - returns false if bag is not empty, prints a message to the user and returns true if backpack is empty.

Related functions
 - *formatItems* - returns formated stacks in a list that is used for printing the backpack to the user
 - *getLengthOfLongestItem* - returns the len of the item with the longest name. Obsolete.
 - *getLengthOfLongestWord* - returns the len of the longest string in a list. Used to determine the final backpack screen size in characters for printing.
 - *createRectangle* - prints a rectange in the console using *formatItems* and *getLengthOfLongestWord*. Examples bellow.
 - *backpackFull* - checks whether backpack is full. If the backpack is full, the funcion takes the player throught the necessary steps to discard some stored or found items in order to continue the game.

How does the backpack look in the console
 - "*" is the backpackSkin
 - "[]" is the slotSkin of the backpack (item info goes in between the brackets)
 - "[-]" is the nullSkin of the backpack
 - "\<rarity>[name]{count}" is the skin of the items in the backpack

Backpack\
![backpack](/Data/Static/backpack.png)
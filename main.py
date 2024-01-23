from Library import game

if __name__ == "__main__":
    game.play()

# TODO create jsonParser to simplify JSON file creation? (a program to create JSON files out of simple .txt, I think it might help with creating different creatures, items, etc.)

#FIXME if backack is full, and item can be added (count can be increased) backpackfull funciton still occurs
#FIXME magic fail occurs twice (whic means it does double damage = BAD) -> only the damage occurs twice? Chicken fail occured once

#FIXME
#  missing console output space
#   - when playerinput receives unknown input
#   - when player uses backack and it is empty
#   - 
    
#FIXME
#  incorect value
#   - when item is consumed, the incorect qty is displayed. Why is the qty displayed in the first place?
    
# TODO remove the "unknown spell" message
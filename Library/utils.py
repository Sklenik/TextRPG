def intro():
    print("Welcome brave adventurer!")

def enterContinue(message, addspacebefore):
    if addspacebefore:
        print('')
    if message != '':
        print(message)
    return input("Press enter to continue...")
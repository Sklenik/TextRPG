# Class Player

class player():
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
    def SetName(self, name):
        self.name = name
    def Name(self):
        return self.name
    def SetHp(self, hp):
        self.hp = hp
    def Hp(self):
        return self.hp
from random import randint
from random import shuffle

class Nation:

    def __init__(self, num, units0):
        self.nation_num = num
        self.numunits = units0
        self.adjacentnations = []

    def addunits(self, units):
        self.numunits += units 

    def removeunits(self, units): 
        self.numunits -= units

    def moveunits(self, units, othernation): 
        self.numunits -= units 
        othernation.numunits += units


class Player:

    def __init__(self, numcaptured):
        self.num = numcaptured
        self.listnations = []

    def add_nation(self, nation):
        self.listnations.append(nation)

    def remove_nation(self, nation): 
        self.listnations.remove(nation)

    def rolldice():
        return randint(1, 6) 

    def highestroll(roll1, roll2, roll3):
        return max(roll1, roll2, roll3)

    def territory_captured(self, playern, nation):
        self.listnations.remove(nation)
        playern.listnations.append(nation)
        self.num -= 1
        playern.num += 1

def attack (attacker, otherplayer, attacknation0, nation0): 
    if attacknation0.numunits == 0 or cannot_attack() == True: 
        return None #must have units in attacking nation

    self_roll = rolldice()
    their_roll = rolldice() 

    while (self_roll == their_roll):
        self_roll = rolldice() 
        their_roll = rolldice() 

    if self_roll > their_roll: 
        othernation.removeunits(1)
        if othernation.numunits == 0: 
            attacking.territory_captured(otherplayer, attacker, nation0)

    else:
        attacknation0.removeunits(1) 
        if attacknation0.numunits == 0: 
            attacker.remove_nation(attacknation0)

    return None
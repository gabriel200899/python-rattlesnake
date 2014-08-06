class Creature(object):
    def __init__(self, name):

        self.name = name

        self.life = 0
        self.mana = 0

        self.gold = 0

        self.strength = 0
        self.charisma = 0
        self.agility = 0

        self.exp = 0
        self.lvl = 1

        self.skills = []

    def take_damage(self, damage):
        if damage >= self.life:
            self.life = 0
        else:
            self.life -= damage
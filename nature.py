import creature
import skill


class Bat(creature.Creature):
    def __init__(self, level):
        super(Bat, self).__init__("Bat")
        self.life = 10 + 5 * level

        self.gold = level * 4

        self.strength = 5 + 2 * level

        self.exp = level ** 2 * 4
        self.lvl = level

    def play(self, target):
        # 0 is attack
        # [0][1] gets the attack_function
        self.skills[0][1](self, target)
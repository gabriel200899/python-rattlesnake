import creature
import skill


class Bat(creature.Creature):
    def __init__(self, level):
        super(Bat, self).__init__("Bat")
        self.life = 10 + 5 * level
        self.level = level
        self.skills.append(skill.attack)
import creature
import skill


class Bat(creature.Creature):
    def __init__(self, level):
        super(creature.Creature, self).__init__()
        self.level = level
        self.skills.update(skill.attack)
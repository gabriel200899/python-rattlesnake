import creature
import skill


class Player(creature.Creature):
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.skills.update(skill.attack)
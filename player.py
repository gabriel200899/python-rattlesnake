import creature
import skill


class Player(creature.Creature):
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.life = 10
        self.skills.append(skill.attack)

    def build(self):
        # interactive player creation
        pass
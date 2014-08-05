from src import creature, skill


class Player(creature.Creature):
    def __init__(self, name):
        super(Player, self).__init__(name)
        self.life = 10
        self.skills.append(skill.attack)
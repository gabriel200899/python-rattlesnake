import creature
import skill


class Player(creature.Creature):
    def __init__(self, name):
        super.__init__()
        self.name = name
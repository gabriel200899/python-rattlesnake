import creature

roles = [["Barbarian", [25, 10, 10, 4, 4, 4, 6, 8]]]


class Player(creature.Creature):
    def __init__(self):
        super(Player, self).__init__("")

    def build(self):
        # interactive player creation
        while True:
            name = input("Name: ")
            if len(name) < 4:
                print("Name must be at least 4 characters long.")
            elif not name[0].isalpha():
                print("Name must start with a letter.")
            else:
                break
        while True:
            print("Choose a role:")
            print_roles()
            index = input("Role: ")
            if index.isdigit() and 0 < eval(index) <= len(roles):
                index = eval(index) - 1
                break
            else:
                print("Invalid index.")

        self.name = name

        self.life = roles[index][1][0]
        self.mana = roles[index][1][1]

        self.strength = roles[index][1][2]
        self.charisma = roles[index][1][3]
        self.agility = roles[index][1][4]
        self.wisdom = roles[index][1][5]
        self.luck = roles[index][1][6]
        self.fat = roles[index][1][7]

    def loot(self, corpse):
        self.exp += corpse.exp
        self.gold += corpse.gold


def print_roles():
    output = []
    for i in range(len(roles)):
        output.append("%5d%20s" % (i + 1, roles[i][0]))
    print('\n'.join(output))
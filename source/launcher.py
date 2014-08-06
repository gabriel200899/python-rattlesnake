from engine import *
from player import Player
from nature import Bat


def main():
    player = Player("Dude")
    bat = Bat(2)
    fight(player, bat)

if __name__ == '__main__':
    main()
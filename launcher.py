from engine import *
from player import Player
from nature import Bat


def main():
    player = Player()
    player.build()
    # please, write a plot for this
    bat = Bat(2)
    fight(player, bat)

if __name__ == '__main__':
    main()
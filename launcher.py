from engine import *
from player import Player
from nature import Bat
from nature import Wolf
from nature import Bear


def main():
    player = Player()
    player.build()
    # please, write a plot for this
    bat = Bat(2)
    wolf = Wolf(1)
    bear = Bear(1)
    fight(player, bat)
    fight(player, wolf)
    fight(player, bear)

if __name__ == '__main__':
    main()

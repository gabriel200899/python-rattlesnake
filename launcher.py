from engine import *
from player import Player
from nature import Bat
from nature import Wolf
from nature import Bear


def main():
    player = Player()
    player.build()
    # please, write a plot for this
    if player.life != 0:
        bat = Bat(2)
        fight(player, bat)
    if player.life != 0:
        wolf = Wolf(1)
        fight(player, wolf)
    if player.life != 0:
        bear = Bear(1)
        fight(player, bear)

if __name__ == '__main__':
    main()

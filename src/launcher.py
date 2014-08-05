from src.engine import *
from src.player import Player
from src.nature import Bat


def main():
    player = Player("Dude")
    bat = Bat(2)
    fight(player, bat)

if __name__ == '__main__':
    main()
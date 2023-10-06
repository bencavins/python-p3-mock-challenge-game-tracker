#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    player = Player('Saaammmm')
    pacman = Game('pacman')
    galaga = Game('galaga')
    Result(player, pacman, 1000)

    ipdb.set_trace()

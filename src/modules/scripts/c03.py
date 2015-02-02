# Book of Life
from constants import *


def effect(card, arena):
    if (MONSTER == card.__name__) and (cardTypes[MONSTER]['ZOMBIE'] == card.monster_type):
        arena.monster_zone[card.name] = arena.graveyard.pop(card)
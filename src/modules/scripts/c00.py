# 7 Completed
from constants import *


def effect(monster, choice):
    if choice == ATTACK:
        monster.atkdef[0] += 700
    elif choice == DEFENSE:
        monster.atkdef[1] += 700
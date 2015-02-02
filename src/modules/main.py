import pygame

import monster
import spell
import trap


m1 = monster.Monster(name='Matazza The Zapper', atkdef=(1300, 1000), nivel=3)
m2 = monster.Monster(name='Alexandrite Dragon', atkdef=(1900, 1500), nivel=4)
print('{0} Vs {1}'.format(m1.name, m2.name))
print(m1.attack(m2))

s = spell.Spell(name='Mystic Typhoon')
print(s.name)

t = trap.Trap(name='Mirror Force')
print(t.name)
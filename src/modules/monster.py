from action import Action


class Monster(Action):
    _defense = False

    def __init__(self, cid=0, name='', monster_type=None, nivel=1,
                 atkdef=(0, 0), description=''):
        """
        @type atkdef: tuple
        """
        self.cid = cid
        self.name = name
        self.monster_type = monster_type
        self.nivel = nivel
        self.atkdef = atkdef
        self.description = description

    def attack(self, monster):
        if monster.isCardFaceDown() or monster.isCardFaceUp():
            self._defense = True
            if not monster.isMonsterNormal():
            # It's a Monster Effect
            # Do Monster's Effect
                return self.calculate_damage(monster, self._defense)
            else:
            # No, it's a Normal Monster. Send it to the Graveyard!
                return self.calculate_damage(monster, self._defense)
        else:
            return self.calculate_damage(monster, self._defense)

    def calculate_damage(self, monster, position):
        if position:
            if self.atkdef[0] > monster.atkdef[1]:
                # Send the Opponent's Monster to the Graveyard
                return
            else:
                damage = self.atkdef[0] - monster.atkdef[1]
                # Keep both monsters, but apply damage

                # return the value as a positive number
                return -damage
        else:
            if self.atkdef[0] > monster.atkdef[0]:
                damage = self.atkdef[0] - monster.atkdef[0]
                # Send the Opponent's Monster to the Graveyard
                return damage
            else:
                damage = self.atkdef[0] - monster.atkdef[1]
                # Send the Player's Monster to the Graveyard
                return -damage
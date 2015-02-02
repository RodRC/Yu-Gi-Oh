class Action(object):
    @staticmethod
    def take_control(monster):
        """The player is able to posses a card for a limited period of time
        @type monster: object
        """
        pass

    @staticmethod
    def pick_up(player):
        """pickUp a card from anywhere
           Ex.: pickUp a card from opponent's hand and see it
        """
        pass

    def draw(self, card, opponent):
        pass

    def shuffle(self):
        pass

    def normalSummon(self):
        pass

    def specialSummon(self):
        pass

    def setCardFaceDown(self, cid):
        pass

    def setCardFaceUp(self, cid):
        return

    def setCardInAttckPosition(self):
        pass

    def flip(self):
        pass

    def send(self):
        pass

    def discard(self):
        pass

    def tribute(self):
        pass

    def destroy(self):
        pass

    def banish(self):
        pass

    def attach(self):
        pass

    def detach(self):
        pass

    def equip(self):
        pass

    def unequip(self):
        pass

    def battleActivate(self):
        pass

    def isCardFaceDown(self):
        pass

    def isCardFaceUp(self):
        pass

    def isMonsterInAttackPosition(self):
        pass

    def isMonsterEffect(self):
        pass

    def isMonsterNormal(self):
        pass

    def activateEffect(self, cid, ct, s):
        """
        cid = card id
        ct = cart type
        s = script
        """
        pass
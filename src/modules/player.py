class Player:
	def __init__(self, deck=40):
		self.hand = []
		self.deck = deck
		self.LP = 8000

	_standByPhase = False

	def drawPhase(self, card, oppononet):
		if oppononet._standByPhase:
			if self.deck > 1:
				if len(self.hand) <= 7:
					self.hand.append(card)
			self.deck -= 1

	def mainPhase(self, arena, card):
		if (len(arena.monster_zone) <= 5 or 
			len(arena.spell_trap_zone) <= 5):
			pass
		else:
			pass

	def battlePhase(self): pass

	def endPhase(self): pass

	def decreaseLP(self, damage):
		self.LP = self.LP - damage
		return self.LP

	def increaseLP(self, additional):
		self.LP = self.LP + additional
		return self.LP

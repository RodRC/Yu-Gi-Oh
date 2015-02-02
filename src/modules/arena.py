class Arena:
	def __init__(self, player):
		self.monster_zone = {}
		self.spell_trap_zone = {}
		self.graveyard = {}
		self.extra_deck = {}
		self.banished = {}
		self.player = player()
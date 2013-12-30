class Battle:
	def __init__(self, player, opponent):
		self.player = player
		self.opponent = opponent
		self.player_botbmon = player.party[0]
		self.opponent_botbmon = opponent.party[0]

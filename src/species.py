class Species:
	def __init__(self, number, name, species, type1, type2, base_stats):
		self.type1 = type1
		self.type2 = type2
		self.base_stats = base_stats
	
	def base_hp(self):
		return self.base_stats[0]

	def base_atk(self):
		return self.base_stats[1]

	def base_def(self):
		return self.base_stats[2]

	def base_spa(self):
		return self.base_stats[3]

	def base_spd(self):
		return self.base_stats[4]

	def base_spe(self):
		return self.base_stats[5]

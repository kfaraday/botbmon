from random import randint
from math import sqrt

class BotBmon:
	def __init__(self, name, species, level):
		self.name = name
		self.species = species
		self.level = level
		self.ivs = [random.randint(0, 15) for i in range(4)]
		self.evs = [0 for i in range(5)]
		self.current_hp = self.hp()
	
	def atk_iv(self):
		return self.ivs[0]
	
	def def_iv(self):
		return self.ivs[1]
	
	def spe_iv(self):
		return self.ivs[2]
	
	# the same iv is used for both special attack and special defense
	def spx_iv(self):
		return self.ivs[3]
	
	def hp_iv(self):
		# the hp iv is determined using the least significant binary
		# digits of the other four scores
		return sum((self.ivs[i] & 1) << (3 - i) for i in range(4))
	
	def hp_ev(self):
		return self.evs[0]

	def atk_ev(self):
		return self.evs[1]

	def def_ev(self):
		return self.evs[2]
	
	def spe_ev(self):
		return self.evs[3]

	# the same ev is used for both special attack and special defense
	def spx_ev(self):
		return self.evs[4]
	
	def hp(self):
		iv = self.hp_iv()
		base = self.species.base_hp()
		ev = self.hp_ev()
		level = self.level
		return ((iv + base + sqrt(ev)/8 + 50) * level) / 50 + 10
	
	# helper method for computing stats
	def non_hp_stat(self, iv, base, ev):
		return ((iv + base + sqrt(ev)/8) * self.level) / 50 + 5
	
	def atk(self):
		iv = self.atk_iv()
		base = self.species.base_atk()
		ev = self.atk_ev()
		return non_hp_stat(iv, base, ev)

	def def(self):
		iv = self.def_iv()
		base = self.species.base_def()
		ev = self.def_ev()
		return non_hp_stat(iv, base, ev)

	def spa(self):
		iv = self.spx_iv()
		base = self.species.base_spa()
		ev = self.spx_ev()
		return non_hp_stat(iv, base, ev)

	def spd(self):
		iv = self.spx_iv()
		base = self.species.base_spd()
		ev = self.spx_ev()
		return non_hp_stat(iv, base, ev)

	def spe(self):
		iv = self.spe_iv()
		base = self.species.base_spe()
		ev = self.spe_ev()
		return non_hp_stat(iv, base, ev)

class Pokemon(object):
	def __init__(self, Name, HP, Atk, Def, Mass):
		self.Name = Name
		self.HP = HP
		self.Atk = Atk
		self.Def = Def
		self.Mass = Mass

	def good(self, Atk, Def):
		if self.Atk and self.Def >= 50:
			return True
		else:
			return False

	def ifRare(self, Name):
		if self.Name == "Charizard" or "Dragonite" or "Snorlax" or "Mewtwo":
			return True
		else:
			return False 

	def ifAttacker(self, Atk, Def):
		if self.Atk >= self.Def:
			return True
		elif self.Atk < self.Def:
			return False
		

	def __str__(self):
		all_variables = (self.Name + " " + str(self.HP) + " " + str(self.Atk) + " " + str(self.Def) + " " + str(self.Mass))
		return all_variables
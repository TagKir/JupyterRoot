class Character:

	def __init__(self, armor, power):
		self.armor = armor
		self.power = power
		self.health = 100

	def hit(self, damage):
		self.health -= damage
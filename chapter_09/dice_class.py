from random import randint

class Dice:
	"""A basic class to represent a dice."""

	def __init__(self, side = 6):
		"""Initial method"""
		self.side = side

	def roll_dice(self):
		"""Method that represents the action of rolling a dice."""
		print(randint(1,self.side))

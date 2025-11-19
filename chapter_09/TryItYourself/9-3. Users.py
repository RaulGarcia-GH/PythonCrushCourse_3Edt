class User:
	"""Basic model of a user"""

	def __init__(self, first_name, last_name, gender, age, height, weight):
		"""Initializing the user's attributes"""
		self.fn = first_name
		self.ln = last_name
		self.gnd = gender
		self.ag = age
		self.ht = height
		self.wt = weight
	
	def describe_user(self):
		"""Method to display user's description"""
		print(f"User name is '{self.first_name.title()}'"
		f" and last name '{self.last_name.title()}'."
		f" The person is '{self.gender.title()}', '{self.age}' years old,"
		f" weights '{self.weight}' and is '{self.height}' tall.")

	def greet_user(self):
		"""Method for user to greet"""
		print(f"Hello, my name is '{self.first_name.title()}'!")


raul = User('raul','garcia','male',52,'1.8 meters', '75 Kgr')
raul.describe_user()
raul.greet_user()

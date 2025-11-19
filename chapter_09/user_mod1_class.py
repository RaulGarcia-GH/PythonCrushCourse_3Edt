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
		print(f"User name is '{self.fn.title()}'"
		f" and last name '{self.ln.title()}'."
		f" The person is '{self.gnd.title()}', '{self.ag}' years old,"
		f" weights '{self.wt}' and is '{self.ht}' tall.")

	def greet_user(self):
		"""Method for user to greet"""
		print(f"Hello, my name is '{self.fn.title()}'!")
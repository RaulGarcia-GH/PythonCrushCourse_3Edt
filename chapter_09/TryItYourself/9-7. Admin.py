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

class Privileges:
	"""A class that helps with Admin's privileges."""

	def __init__(self):
		"""Initialize"""
		self.privileges = ["can add post", "can delete post", "can ban user"]

	def show_privileges(self):
		"""Print the each privilege in the self.privileges list. """

		for privilege in self.privileges:
			print(privilege.title())

class Admin(User):
	"""A class that inherites user and have different"""

	def __init__(self, first_name, last_name, gender, age, height, weight):
		"""
		Initializes with the parent's attributes
		and priviliges
		"""
		super().__init__(first_name, last_name, gender, age, height, weight)
		self.privileges = Privileges()

	
raul = Admin('raul','garcia','male',52,'1.8 meters', '75 Kgr')
raul.describe_user()
raul.greet_user()
#raul.show_privileges()
raul.privileges.show_privileges()


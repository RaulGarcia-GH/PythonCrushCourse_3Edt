from user_mod1_class import User

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

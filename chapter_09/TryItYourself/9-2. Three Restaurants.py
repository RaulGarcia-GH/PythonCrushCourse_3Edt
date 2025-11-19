class Restaurant:
	"""A class to model restaurants"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize atributes restaurant_name and cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		"""Brief description of the restuarant"""
		print(f"'{self.restaurant_name.title()}' is a restaurant that specialises in {self.cuisine_type.title()} cuisine.")

	def open_restaurant(self):
		"""Brief message that the restaurant is open"""
		print(f"Restaurant '{self.restaurant_name.title()}' is now open for business.")


first = Restaurant('la masia','catalan')
second = Restaurant('oban in','scotish')
third = Restaurant('la grola','italian')

first.describe_restaurant()
second.describe_restaurant()
third.describe_restaurant()

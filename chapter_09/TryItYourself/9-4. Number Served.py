class Restaurant:
	"""A class to model restaurants"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize atributes restaurant_name and cuisine_type"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
		
	def describe_restaurant(self):
		"""Brief description of the restuarant"""
		print(f"'{self.restaurant_name.title()}' is a restaurant that specialises in {self.cuisine_type.title()} cuisine.")

	def open_restaurant(self):
		print(f"Restaurant '{self.restaurant_name.title()}' is now open for business.")
	
	def set_number_served(self, quantity):
		self.number_served = quantity

	def increment_number_served(self, quantity):
		self.number_served += quantity

restaurant = Restaurant('la masia','catalan')

print(restaurant.number_served)

restaurant.number_served = 25

print(restaurant.number_served)

restaurant.set_number_served(150)

print(restaurant.number_served)

restaurant.increment_number_served(265)

print(restaurant.number_served)

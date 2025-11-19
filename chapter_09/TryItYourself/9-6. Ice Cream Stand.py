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
		"""Prints statement that the restaurant is open."""
		print(f"Restaurant '{self.restaurant_name.title()}' is now open for business.")


class IceCreamStand(Restaurant):
	"""A class that inherites Restaurant class"""

	def __init__(self, restaurant_name, cuisine_type):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an Ice Cream Stand.
		"""
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = ('strawberry','vanilla','chocolate')

	def display_flavours(self):
		for flavor in self.flavors:
			print(flavor.title())


my_ice_cream_stand = IceCreamStand('Hoo foo','british')
my_ice_cream_stand.open_restaurant()
my_ice_cream_stand.display_flavours()
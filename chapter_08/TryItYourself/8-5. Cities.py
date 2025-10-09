def describe_city(city, country = 'catalonia'):
	"""Return a message with city and country."""
	print(f"We all know that {city.title()} is in {country.title()}.")

describe_city('girona')
describe_city(city = 'barcelona')
describe_city(city = 'madrid')
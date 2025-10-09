def city_country(city, country):
	value = f'"{city}, {country}"'
	return value.title()

value = city_country('barcelona','catalonia')
print(value)

value = city_country('london','england')
print(value)

value = city_country('paris','france')
print(value)
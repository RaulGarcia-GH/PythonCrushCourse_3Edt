cities = {
	'barcelona' : {'country':'catalonia', 'population':'4 million', 'fact':'it is beautiful'},
	'lisbon' : {'country':'portugal', 'population':'2 million', 'fact':'it is by the ocean'},
	'rome' : {'country':'italy', 'population':'3 million', 'fact':'has great food'}
}

for city, facts in cities.items():
	print(f"{city.title()} is in {facts['country'].title()}, has a population of {facts['population']} and {facts['fact']}.")
fav_numbers = {
	'raul': [1, 3, 5],
	'louise': [40, 58, 50],
	'melanie': [18, 28, 38],
	'jasmine': [1, 11, 23],
	'laila': [15, 25],
}



for person, numbers in fav_numbers.items():
	numbs = ''
	for number in (numbers):
		numbs += f"{number}, " 
	print(f"\n{person.title()}'s favourite numbers are: {numbs}")


fav_numbers = {
	'raul':3,
	'louise':5,
	'melanie':11,
	'jasmine':1,
	'laila':15,
}

for num in fav_numbers:
	print(f"{num.title()}'s favourite number is: {fav_numbers[num]}")

print('\nAdding Ana and Edu\n')
fav_numbers['edu'] = 20
fav_numbers['ana'] = 17

for num in fav_numbers:
	print(f"{num.title()}'s favourite number is: {fav_numbers[num]}")

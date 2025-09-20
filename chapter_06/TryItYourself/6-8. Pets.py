dog = {
	'pet': 'dog',
	'pet_name': 'doggie',
	'pet_owner': 'laila'
}

cat = {
	'pet': 'cat',
	'pet_name': 'cattie',
	'pet_owner': 'jasmine'
}

rabbit = {
	'pet': 'rabbit',
	'pet_name': 'rab',
	'pet_owner': 'louise'
}

pets = [dog]

pets.append(cat)
pets.append(rabbit)

#print(pets)

for pet in pets:
	print(f"Type of Pet:{pet['pet'].title()}  -  Pet's Name: {pet['pet_name'].title()}  -  Pet's Ower: {pet['pet_owner'].title()}\n")
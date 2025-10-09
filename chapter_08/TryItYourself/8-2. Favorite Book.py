def describe_pet(pet_name, animal_type='dog'):
	"""Function to display information about a pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('berto')
describe_pet(pet_name='sisco', animal_type='cat')
# describe_pet(pet_name='marcos', animal_type='parrot')

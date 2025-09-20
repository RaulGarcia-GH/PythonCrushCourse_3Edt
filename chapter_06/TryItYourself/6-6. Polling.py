favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'rust',
	'phil': 'python',
}
poll_people = {'pete','jen','andy','lewis','edward','paul'}

for person in favorite_languages.keys():
	if person in poll_people:
		print(f"{person.title()} thanks for responding.")
	else:
		print(f"{person.title()} please consider taking the poll.")

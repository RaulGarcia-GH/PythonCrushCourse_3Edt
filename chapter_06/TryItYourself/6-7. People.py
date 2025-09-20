fat = {
	'first_name': 'louise',
	'last_name': 'garcia',
	'age': 47,
	'city': 'burguers',
	'DoB': '1978-04-09',
}
master = {
	'first_name': 'raul',
	'last_name': 'garcia',
	'age': 52,
	'city': 'burguers',
	'DoB': '1973-06-07',
}
girl1 = {
	'first_name': 'melanie',
	'last_name': 'garcia',
	'age': 28,
	'city': 'london',
	'DoB': '1997-05-25',
}
girl2 = {
	'first_name': 'jasmine',
	'last_name': 'garcia',
	'age': 18,
	'city': 'burguers',
	'DoB': '2007-03-14',
}
girl3 = {
	'first_name': 'laila',
	'last_name': 'garcia',
	'age': 15,
	'city': 'burguers',
	'DoB': '2010-02-05',
}

fam = [master, fat, girl1, girl2, girl3]

count = 0
for fm in fam:
	count += 1
	print(f"\n{count} - Member:")
	for key, val in fm.items():
		if key == 'age':
			print(f"\t{key.title()}: {val}")
		elif key == 'DoB':
			print(f"\t{key}: {val.title()}")
		else:
			print(f"\t{key.title()}: {val.title()}")

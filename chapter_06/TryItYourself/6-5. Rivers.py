rivers = {
	'nile':'egipt',
	'amazonas':'brazil',
	'mississipi':'usa'
}

for key, value in rivers.items():
	if value == 'usa':
		value = value.upper()
	else:
		value = value.title()
	print(f'{key.title()} runs through {value}')
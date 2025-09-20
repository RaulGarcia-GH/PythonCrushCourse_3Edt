favority_places = {
	'emma': ['madrid','rome','paris'],
	'pete': ['barcelona','london'],
	'chris': ['lisbon','milan','berlin']
}
for person, places in favority_places.items():
	print(f"\n{person.title()}'s favourite places are:")
	for place in places:
		print(f"  - {place.title()}")
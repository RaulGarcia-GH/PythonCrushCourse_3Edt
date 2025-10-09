def make_album(artist, album, number_of_songs = None):
	lp = {'artist' : artist, 'album' : album}
	if number_of_songs:
		lp['number_of_songs'] = number_of_songs
	return lp

while True:
	print("\nWhat are your favourite artist and album?")
	print("Type 'q' to quit")

	artist = input("\nArtist: >>> ")
	if artist.lower() == 'q':
		break

	album = input("Album: >>> ")
	if album.lower() == 'q':
		break

	output = make_album(artist,album)
	print(output)


# album = make_album('Sting','Englishman in New York')
# print(album)

# album = make_album('Dire Straits','Making Movies',15)
# print(album)

# album = make_album('Victor Manuel y Ana Belen','Mucho mas que dos')
# print(album)
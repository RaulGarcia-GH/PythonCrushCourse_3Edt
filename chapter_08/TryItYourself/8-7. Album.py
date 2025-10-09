def make_album(artist, album, number_of_songs = None):
	lp = {'artist' : artist, 'album' : album}
	if number_of_songs:
		lp['number_of_songs'] = number_of_songs
	return lp

album = make_album('Sting','Englishman in New York')
print(album)

album = make_album('Dire Straits','Making Movies',15)
print(album)

album = make_album('Victor Manuel y Ana Belen','Mucho mas que dos')
print(album)
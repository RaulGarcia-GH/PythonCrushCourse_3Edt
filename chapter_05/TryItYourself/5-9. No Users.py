usernames = []

if usernames:
	for username in usernames:
		if username == 'admin':
			print(f"Hello {username.title()}, would you like to see a status report?\n")
		else:
			print(f"Hello {username.title()}, thank you for logging in again.\n")
else:
	print('We need to find some users!')
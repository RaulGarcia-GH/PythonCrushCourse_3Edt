message = input("How many of you?: ")
message = int(message)

if message > 8:
	print ("You need to wait for a table.")
else:
	print("Your table is ready.")
message = input("Please insert a number: ")
message = int(message)

if message % 10 == 0:
	print("You provided and number that is a multiple of 10")
else:
	print("The number provided is not a multiple of 10")
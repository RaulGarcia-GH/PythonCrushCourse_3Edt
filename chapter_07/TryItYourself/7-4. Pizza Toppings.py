message = "\nPlease add toppings to your pizza:"
message += "\nType 'quit' to finish  >>>  "

topping = ""
while topping != 'quit':
	topping = input(message).lower()

	if topping != 'quit':
		print(f"\nYou have added '{topping}' to your pizza.")

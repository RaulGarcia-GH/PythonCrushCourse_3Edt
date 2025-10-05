message = "\nHow old are you?"
message += "\nEnter your age here >>> "

age = input(message)
age = int(age)

if age < 3:
	print(f"\nYou are '{age}' it is free for you.")
elif age < 13:
	print(f"\nYou are '{age}' it is $10 for you.")
else:
	print(f"\nYou are '{age}' it is $12 for you.")
		

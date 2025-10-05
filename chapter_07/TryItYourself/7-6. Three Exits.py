message = "\nHow old are you?"
message += "\nEnter your age here (type 99 to exit) >>> "

# Conditional
# age = 0
# while age < 99:

# 	age = input(message)
# 	age = int(age)

# 	if age < 3:
# 		print(f"\nYou are '{age}' it is free for you.")
# 	elif age < 13:
# 		print(f"\nYou are '{age}' it is $10 for you.")
# 	else:
# 		print(f"\nYou are '{age}' it is $12 for you.")

# active variable
# active = True
# while active:

# 	age = input(message)
# 	age = int(age)

# 	if age < 3:
# 		print(f"\nYou are '{age}' it is free for you.")
# 	elif age < 13:
# 		print(f"\nYou are '{age}' it is $10 for you.")
# 	elif age <99:
# 		print(f"\nYou are '{age}' it is $12 for you.")
# 	else:
# 		active = False

message = "\nHow old are you?"
message += "\nEnter your age here (type 'quit' to exit) >>> "

while True:

	age = input(message).lower()
	if age == 'quit':
		break
	else:
		age = int(age)

		if age < 3:
			print(f"\nYou are '{age}' it is free for you.")
		elif age < 13:
			print(f"\nYou are '{age}' it is $10 for you.")
		elif age >= 13:
			print(f"\nYou are '{age}' it is $12 for you.")

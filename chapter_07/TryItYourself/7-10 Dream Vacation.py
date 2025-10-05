vacations = {}
status = True

#while status:
while True:
	name = input("\nWhat is you name? >>> ")
	message = input("If you could visit one please in the world where would you go? >>> ")
	vacations[name] = message
	
	flag = input("\nDo you want to enter another person? (Yes/No) >>>")

	if flag.lower() == 'no':
#		status = False
		break

print("*** Pol Results ***")
for name, message in vacations.items():
	print(f"  - {name.title()} would like to visit {message.title()}")

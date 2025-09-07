print("Buffet Menu:")
buffet = ('pizza','pasta','fish','wine','lamb','beef')
for food in buffet:
	print(f"  - {food.title()}")

#print("\nModify item in tuple")
#buffet[2] = 'pork'

print("\nRewrite Menu:")
buffet = ('pizza','pasta','sea food','water','lamb','beef')
for food in buffet:
	print(f"  - {food.title()}")

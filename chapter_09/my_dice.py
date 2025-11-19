from dice_class import Dice

my_dice = Dice(10)

count = 1

while count <= 10:
	my_dice.roll_dice()
	count += 1
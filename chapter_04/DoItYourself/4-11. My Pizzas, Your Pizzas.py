pizzas = ['margarita','pepperoni','romana']
friend_pizzas = pizzas[:]

pizzas.append('nduja')

friend_pizzas.append('diabola')

print("My favourite pizzas are:")
for pizza in pizzas:
	print(f"\t{pizza.title()}")

print("\nMy friend's favourity pizzas are:")
for pizza in friend_pizzas:
	print(f"\t{pizza.title()}")
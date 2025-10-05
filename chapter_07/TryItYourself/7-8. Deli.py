sandwich_orders = ['tuna','bacon','chicken']

finished_sandwiches = []

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"\nI've made you a '{sandwich.title()}' sandwich.")
	finished_sandwiches.append(sandwich)

print("\n*** Sandwiches made ***")
for item in finished_sandwiches:
	print(f"  - {item.title()}")
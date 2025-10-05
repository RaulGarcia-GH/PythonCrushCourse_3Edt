sandwich_orders = ['pastrani','tuna','pastrani','bacon','pastrani','chicken']

finished_sandwiches = []

print("\n*** IMPORTANT: sorry we have run out of Pastrani Sandwiches ***")

while 'pastrani' in sandwich_orders:
	sandwich_orders.remove('pastrani')

while sandwich_orders:
	sandwich = sandwich_orders.pop()
	print(f"\nI've made you a '{sandwich.title()}' sandwich.")
	finished_sandwiches.append(sandwich)

print("\n*** Sandwiches made ***")
for item in finished_sandwiches:
	print(f"  - {item.title()}")
def make_sandwich(*items):
	"""Creates a list of the items contained in a sandwich"""
	print("\nSandwich created with the following items:")
	for item in items:
		print(f"  - {item.title()}")

make_sandwich('bacon','tomato','letuce')
make_sandwich('chicken','bacon','mayo')

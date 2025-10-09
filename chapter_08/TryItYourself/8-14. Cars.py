def make_car(make, model, **opt_features):
	"""Create a dictionary about a car"""
	opt_features['make'] = make
	opt_features['model'] = model
	return opt_features

made_car = make_car('subaru', 'outback', color = 'blue', tow_package = True)
print(made_car)
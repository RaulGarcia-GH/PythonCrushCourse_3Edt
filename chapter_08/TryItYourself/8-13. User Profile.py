def build_profile(first, last, **user_info):
	"""Create a profile, given the first and last names plus an unknown number of key-value pairs"""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

built_profile = build_profile('raul','garcia',edad=40, altura=1.78, peso=75, ciudad='barcelona')
print(built_profile)
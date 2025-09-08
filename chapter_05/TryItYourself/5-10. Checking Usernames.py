current_users = ['Smith','Tibot','Olek','Ben','Urrik']
current_user_lw = []
new_users = ['Smith','Troy','Oman','BEN','Ortiz']

for current_user in current_users:
	current_user_lw.append(current_user.lower())

for new_user in new_users:
	if new_user.lower() not in current_user_lw:
		print(f"Username {new_user.lower()} is available.\n")
	else:
		print(f"Username {new_user.lower()} is not available, enter a new surname.\n")


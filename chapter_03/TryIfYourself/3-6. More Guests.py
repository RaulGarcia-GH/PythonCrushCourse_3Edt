guest_list = []
guest_list.append('pablo')
guest_list.append('edu')
guest_list.append('alberto')

print(guest_list)

guest_list.insert(0, 'piru')
guest_list.insert(2, 'raquel')
guest_list.append('rosa')

print(guest_list)

for x in guest_list:
	print(f"Bienvenido/a a mi fiesta {x.title()}")

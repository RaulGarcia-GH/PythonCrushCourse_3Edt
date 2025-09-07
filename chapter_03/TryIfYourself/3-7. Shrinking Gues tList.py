guest_list = []
guest_list.append('pablo')
guest_list.append('edu')
guest_list.append('alberto')

guest_list.insert(0, 'piru')
guest_list.insert(2, 'raquel')
guest_list.append('rosa')

print(guest_list)

adios = guest_list.pop(0)
print(f"Lo siento {adios.title()} pero no puedes asistir a mi fiesta. Un saludo.")

adios = guest_list.pop(0)
print(f"Lo siento {adios.title()} pero no puedes asistir a mi fiesta. Un saludo.")

adios = guest_list.pop(0)
print(f"Lo siento {adios.title()} pero no puedes asistir a mi fiesta. Un saludo.")

adios = guest_list.pop()
print(f"Lo siento {adios.title()} pero no puedes asistir a mi fiesta. Un saludo.")

print(guest_list)

for x in guest_list:
	print(f"Enhora buena estás invitado a mi fiesta {x.title()}")

del guest_list[1]
del guest_list[0]

print(guest_list)


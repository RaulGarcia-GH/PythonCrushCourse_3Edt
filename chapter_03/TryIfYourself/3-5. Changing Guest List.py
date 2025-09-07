guest_list = []
guest_list.append('pablo')
guest_list.append('edu')
guest_list.append('alberto')

print(guest_list)


print(f"{guest_list.pop(2).title()} can't make it")

print(guest_list)
print(f"Bien venido {guest_list[0].title()}")
print(f"Bien venido {guest_list[1].title()}")

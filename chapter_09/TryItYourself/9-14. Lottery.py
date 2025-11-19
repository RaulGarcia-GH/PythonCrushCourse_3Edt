from random import choice

lst = ['r', 's', 'a', 'z', 'x', 1, 3, 5, 7, 9, 11, 25, 33, 45, 69]

fn_chc = []

counter = 0
while counter < 5:
	fn_chc.append(choice(lst))
	counter += 1

print(fn_chc)
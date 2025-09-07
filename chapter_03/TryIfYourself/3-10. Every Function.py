servers = []
servers.append('dt-garcia')
servers.append('xnb-garcia')
servers.append('rnb-garcia')
servers.append('lnb-garcia')
servers.append('jlt-garcia')
servers.append('llt-garcia')
servers.append('nb-garcia')
servers.append('rlt-garcia')
servers.append('dt-essen')
servers.append('dt-nbx-garcia')
servers.append('dt-rltx-garcia')
servers.append('dt-nb-garcia')

print(servers)

print(servers[-1])
print(servers[-2])

servers.insert(5,'dt-nb-garcia')
print(servers)

del servers[5]
print(servers)

servers.remove('dt-essen')
print(servers)

servers.pop()
print(servers)

servers.pop(7)
print(servers)

qty = len(servers)
print(qty)

servers.reverse()
print(servers)

servers.reverse()
print(servers)

servers.sort()
print(servers)

servers.sort(reverse=True)
print(servers)

asc_sort =  sorted(servers)
print(asc_sort)

desc_sort =  sorted(servers, reverse=True)
print(desc_sort)

for server in servers:
	print(f"\nThis is server {server.upper()} and works correctly.")
	print("Este servidor es parte the mi red personal.")

print(servers[-1])
del servers[-1]
print(servers[-1])


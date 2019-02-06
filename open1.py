l=[]
with open("running-config.cfg","rt") as in_file:
	for interface in in_file:
		l.append(interface)


interface=[]
vlan=[]
name=[]
ip_address=[]
mac_address=[]
for i in l:
	a=""
	b=""
	t=i.split()

	if(t[0]=="interface"):
		interface.append(t[1])
	if(t[0]=="vlan"):
		vlan.append(t[1])
	if(t[0]=="nameif"):
		name.append(t[1])
	if(t[0]=="ip"):
		ip_address.append(t[2])
		mac_address.append(t[3])


print("Interface")
print(interface)


print("Vlan")
print(vlan)


print("Name")
print(name)


print("Ip address")
print(ip_address)

print("Mac addres:")
print(mac_address)


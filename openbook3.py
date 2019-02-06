l=[]
with open("running-config.cfg","rt") as in_file:
	a=in_file.read()
        #for interface in in_file:
         #       l.append(interface)
b=a.split("!")
print(b)
#for i in l:
#	print(i)

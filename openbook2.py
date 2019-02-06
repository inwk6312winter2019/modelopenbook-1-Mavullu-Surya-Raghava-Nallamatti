with open('running-config.cfg') as f:
 newText=f.read().replace('192', '10')
 newText=f.read().replace('172', '10')

print(newText)

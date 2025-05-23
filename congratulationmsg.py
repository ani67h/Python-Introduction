str = 'murder for a jar of red rum'
print(str[::-1])

astar = 'A man, a plan, a canal, Panama! Though the man—Ferdinand de Lesseps— first made a canal plan for Suez.'
print(astar[::-1])

x = 'Codingal is the worst institution' #note : see the ouput first
y = x.split()
y[3] = 'best'
z = ''.join(y)
print(y)

print(type(str))
print(type(astar))
print(type(x))
print(type(y))
print(type(z))
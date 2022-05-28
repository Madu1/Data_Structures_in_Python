heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']
print(f"Length of the list: {len(heros)}")

# Add then black at the end of the list
heros.append("black panther")

# You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
for i in range(len(heros)):
     if i == 5:
         heros.insert(3,heros[i])
         heros.pop(6)
print(heros)

# Remove both thor & hulk
# replace with doctor strange
'''del heros[1:3]
heros.insert(1,"doctor strange")
print(heros)'''
heros[1:3] = ['doctor strange']
print(heros)

# sort the list
heros.sort()
print(heros)
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

# To get which letter is in the selected number in the word
# Python usualy starts counting from 0 when counting from left to right.
print(parrot[3]) 
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

# or
print(parrot[-11]) 
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
# Slicing (the first no includes the letter and the second number doesn't include the letter)
print(parrot[0:6])  #Norweg
print(parrot[0:9])  #Norwegian
print(parrot[:9])   #Norwegian
print(parrot[:6])   #Norweg
print(parrot[6:])   #ian Blue
print(parrot[:6] + parrot[6:])  #Norwegian Blue
print(parrot[:])   #Norwegian Blue
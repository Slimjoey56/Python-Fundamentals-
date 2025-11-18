#String Slicing: Extracting Substrings with Start,
# Stop, and Step Values in Python
#          01234567891234
parrot =  "Norwegian Blue"

#formular for slicing in python:
#[start:stop:step]


#slicing without a step
#note [start:stop] it start from index 0
#and the stop index is not included
print(parrot[0:6]) #Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])

#mini challenge slice to produce the word Blue
print(parrot[10:14])
print(parrot[10:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

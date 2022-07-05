myDict = {'a':15 , 'c':35, 'b':10}

keys = myDict.keys()
print("Keys:",list(keys))
print("Values:",list(myDict.values()))
print("Key-Value pairs:")

for i in myDict:
    print(i,myDict[i])
print("/n")

print("Key value pairs- sorted by key")
for i in sorted(myDict):
    print(i,myDict[i])

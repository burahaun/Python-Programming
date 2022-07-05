import random
x = input("Enter the name of the file to which results should be written: ")
file = open(x, 'w')
y = int(input("Enter the number of random numbers to be written to the file: "))
for i in range(y):
    L = str(random.randint(1,100))
    L = L + "\n"
    file.write(L)
file.close()
        


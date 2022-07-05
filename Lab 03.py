def cel2far(c):
   f=(9 / 5) * c + 32
   return f

def far2cel(f):
    c=(5 / 9) * (f - 32)
    return c

c=int(input("Enter a number for celsius"))
print("Celsius to Fahrenheit")
for c in range( 0, c+1, 1):
    cel2far(c)
    print("celsius:", c, "fahrenheit:" , cel2far(c))

f=int(input("Enter a number for Fahrenheit:"))
print("Fahrenheit to Celsius")
for i in range (0, f+1, 1):
    far2cel(i)
    print("Celsius:", far2cel(i), "Fahrenheit:", i)

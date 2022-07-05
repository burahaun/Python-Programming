a = input("Enter a string: ")
b = input("Enter another string: ")
def string(a,b):
    if len(a) > len(b):
        return a[1:].upper()
    else:
        return b[1:].upper()
      

print("The new string is:",string(a,b))
    

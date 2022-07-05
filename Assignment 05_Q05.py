def histogram():
    x = input("Enter a string: ")
    L = list(set(x))
    L.sort()
    sum = 0
    for i in L:
        if i != " ":
            sum = x.count(i)
            print(str(i).upper(),end=" ")
            print(sum*" * ")


       
histogram()
    

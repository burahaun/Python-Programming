while True:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print("The sum of the numbers you entered is",float(x+y))
    z = input("Do you want to do that again? (y/n): ")
    if z == "y":
        continue
    else:
        break

    

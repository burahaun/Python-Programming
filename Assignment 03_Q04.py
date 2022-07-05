p1 = input("Enter the first primary color in lower case letters: ")
if p1 == "red" or "blue" or "yellow":
    p2 = input("Enter the second primary color in lower case letters: ")
    if p2 == p1:
        print("Error: The two colors you entered are the same")
    elif p1 == "red" and p2 == "blue":
        print("When you mix the primary colors red and blue the resulting color is purple")
    elif p1 == "red" and p2 == "yellow":
        print("When you mix the primary colors red and yellow the resulting color is orange")
    elif p1 == "yellow" and p2 == "blue":
        print("When you mix the primary colors yellow and blue the resulting color is green")
    elif p2 != "red" or "blue" or "yellow":
        print("Error: The second color you entered is invalid")
else:
    print("Error: The first color you entered was invalid")

    


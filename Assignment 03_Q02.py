senior_citizens=0
non_senior=0
for i in range(10):
    age = int(input("Enter age: "))
    if age >= 65:
        senior_citizens = senior_citizens + 1
    else:
        non_senior = non_senior + 1
   
print("The number of senior citizens is", senior_citizens)
print("The number of non senior citizens is", non_senior)

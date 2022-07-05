class_a = 15
class_b = 12
class_c = 9

a_seat = int(input("Enter count of A seats: "))
b_seat = int(input("Enter count of B seats: "))
c_seat = int(input("Enter count of C seats: "))

a = class_a * a_seat
b = class_b * b_seat
c = class_c * c_seat

print("Income from class A seats: $",a_seat * class_a)
print("Income from class A seats: $",b_seat * class_b) 
print("Income from class A seats: $",c_seat * class_c)

d = a + b + c
print("Total income:$",d)

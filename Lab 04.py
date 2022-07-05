speed = int(input("Enter the speed of the vehicle in mph: "))
time = int(input("Enter the number of hours traveled: "))
def distance(speed,time):
    print("Hour          Distance Traveled")
    print("-------------------------------")
    for i in range(1,time+1):
        distance = i * speed
        print(i,"\t\t",45*i)
    totaldistance = 0
    for i in range(time+1):
        totaldistance = totaldistance + distance
    print("The accumulated distance traveled is: ", totaldistance//2)
        
distance(speed,time)


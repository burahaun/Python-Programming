import math
def convertMillis(millis):
    millis = int(input("Enter time in milliseconds: "))
    hour = math.floor((millis/3600000)%24)
    minute = math.floor((millis/60000)%60)
    second = math.floor((millis/1000)%60)
    time = str(int(hour))+":"+str(int(minute))+":"+str(int(second))
    return(time)

print(convertMillis(55550000))

import time

timeNow=time.gmtime()

def currentTime(timeNow):
    timeNow=time.asctime(timeNow)
    return timeNow

clock=currentTime(timeNow)

print("The current time is "+str(clock)+"GMT")

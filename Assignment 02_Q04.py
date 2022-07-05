foot = 10
meter = 65
def footToMeter(foot, meter):
    for i in range(1, foot+1,1):
        meter = 0.305 * i
        print(i,"\t\t\t",meter)
print(" ")
print("Feet\t\t\tMeters\t\t\t")
print("----------------------------------")
footToMeter(foot,meter)

def meterToFoot(meter, foot):
    for i in range(20, meter+1,5):
        foot = i/0.305
        print(i,"\t\t\t",foot)
print(" ")
print("Feet\t\t\tMeters\t\t\t")
print("----------------------------------")
meterToFoot(meter,foot)

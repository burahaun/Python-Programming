datah = []
datal = []
x=print("Enter the highest temperatures for 12 months")
print("\n")
high = (input().split())
for i in range(len(high)):
    hightem = float(high[i])
    datah.append(hightem)

y=print("\nEnter the lowest temperatures for 12 months")
print("\n")
low = (input().split())
for i in range(len(low)):
    lowtem = float(low[i])
    datal.append(lowtem)


def getData():
    print("\nList of the highest and lowest temperatures for each month of the year")

    data = [datah, datal]
    for r in range(len(data)):
        for c in range(len(data[r])):
            print(data[r][c], end = " ")
        print()

def averageHigh(datah):
    sumHigh = 0
    for i in range(0,len(datah)):
        sumHigh += datah[i]
    average = sumHigh/len(datah)
    return average

def averageLow(datal):
    sumLow = 0
    for i in range(len(datal)):
        sumLow += datal[i]
    average = sumLow /len(datal)
    return average

def highTemp(datah):
    return max(datah)

def lowTemp(datal):
    
    return min(datal)


getData()
print("\n")
print("Average high temperature for the year ", averageHigh(datah))
print("Average low temperature for the year ",averageLow(datal))
print("Highest high temperature for the year ",highTemp(datah))
print("lowest low temperature for the year ", lowTemp(datal))

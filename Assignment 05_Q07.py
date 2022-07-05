v = "Fahrenheit       Celcius   \n"

for i in range(-10,10):
    c = (i-32)*5/9
    v = v + "{:12.2f}".format(i)+" "
    v = v + "{:12.2f}".format(c)+"\n"
x = open("temp.txt","w")
x.write(v)
x.close()

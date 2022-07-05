dic1 = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
dic2 = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
dic3 = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}


x = input("Enter a course a number: ")
for i in range(1):
    if x not in dic1:
        print("CS105 is an invalid course number")
    if x in dic1:
        print("The details for course",x,"are:")
        print("Room:",dic1['CS103'])
        print("Instructor:",dic2['CS103'])
        print("Time:",dic3["CS103"])
                        
       


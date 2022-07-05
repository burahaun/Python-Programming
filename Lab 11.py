def twoD(array):
    L = []
    print("2D LIST")

    for i in array:
        count = 0
       
        for j in i:

            print("{:2}".format(j) , end= " ")
           
            if j>0 and j%2==0:
                count+=1

        L.append(count)
        print()
       
    print()
    print("Number of even non negative values")

    for i in range(0, len(L)):

        print("Row {} : {}".format(i, L[i]))

    return L

array = [[2,3,5], [-8,4,6],[9,3,77],[11,-2,9]]
twoD(array)

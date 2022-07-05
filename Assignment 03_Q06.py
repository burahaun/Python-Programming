def prob6(l1,w1,l2,w2):
    areaA = l1 * w1
    areaB = l2 * w2
    print("Area A:",areaA)
    print("Area B:",areaB)
    if areaA == areaB:
        print("Area A is equal to Area B")
    elif areaA >= areaB:
        print("Area A is greater than Area B")
    else:
        print("Area B is greater than Area A")

prob6(3,4,4,3)
    

def swap_pairs(swap):
    str(swap)
    newString = ""
    for i in range(0,len(swap)-1,2):
        newString = newString + swap[i+1]
        newString = newString + swap[i]
    if len(swap) % 2 != 0:
        newString = newString + swap[len(swap)-1]
    print(swap,"->",newString)

swap_pairs("example")

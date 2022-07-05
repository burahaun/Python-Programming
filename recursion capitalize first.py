def capitalizeFirst(arr):
    for i in arr:
        arr[i].upper()
    return arr
    
print(capitalizeFirst(["car","taco","banana"]))

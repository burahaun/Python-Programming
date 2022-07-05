print("First Nested Loop:\n")

for i in range(1, 8):
    for j in range(1, i+1):
        print('*', end='')
    print()


print("\nSecond Nested Loop\n")

for i in range(7,0,-1):
    for j in range(1,i+1):
        print('*', end='')
    print()

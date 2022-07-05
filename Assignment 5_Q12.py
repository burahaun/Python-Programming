x = int(input("Type a number: "))
def print_average(x):
    if x < 0:
        print("Average was 0:")
    else:
        t = x
        acc = 1
        x = int(input("Type a number: "))
        while x >= 0:
            t = t + x
            acc = acc + 1
            x = int(input("Type a number: "))
        print("Average was",(t/acc))

print_average(x)

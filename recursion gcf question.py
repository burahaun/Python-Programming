#Calculate GCF between two numbers

def gcf(n1,n2):
    if n1 % n2 == 0:
        return n2
    else:
        return n1%n2


print(gcf(48,16))
        

import string
alpha = "abcdefghijklmnopqrstuvwxyz"
acc = {}
para = ""
file = open(input("Enter a file name: "),'r')

for i in file:
    para = para + i
    para = para.lower()
    for j in para:
        if j in string.punctuation:
            para = para.replace(j,"")

print("Letter                 Count")
for k in string.ascii_lowercase:
    acc[k] = para.count(k)
for keys,values in acc.items():
    print(keys +"                              "+str(values))

file.close()


            
    

def repl(str,num):
    if num <= 0:
        print('a')
    else:
        for i in range(num):
            print(str,end='')
        

print("hello -> ",end=''),repl('hello',3)
 

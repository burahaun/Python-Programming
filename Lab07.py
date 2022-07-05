str1 = input("Enter a string: ")
ch = input("Enter a charatcer: ")
def countLetters(str1,ch):
    newStr = 0
    for i in range(len(str1)):
        if str1[i] == ch:
            newStr = newStr + 1
    return newStr

print(countLetters(str1,"e"))
        
str2 = input("Enter a string: ")
def countDigits(str):
    digit = 0
    num = "0123456789"
    for i in range(len(str2)):
        if str2[i] in num:
            digit = digit + 1
    return digit

print("The number of digits in",str2,"is",countDigits(str2))
        

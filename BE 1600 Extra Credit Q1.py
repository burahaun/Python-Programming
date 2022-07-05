def encryption(plainText):
    one=""
    two=""
    three=""
    charCount=0
    for c in plainText:
        if charCount%3==0:
            one = one + c
        elif charCount%3==1:
            two = two + c
        else:
            three = three + c
           
        charCount = charCount +1 
       
    cipherText = three+two+one
    return cipherText
   
   
print("Plain text: ABCDEFGHI","\n","Cipher Text:",encryption('ABCDEFGHI'))
print("Plain text: JACK IN THE BOX","\n","Cipher Text:",encryption('JACK IN THE BOX'))

def substitutionDecrypt(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    cipherText = cipherText.lower()
    plainText = ""
    for i in cipherText:
        idx = alphabet.find(i)
        plainText = plainText + key[idx]
    return plainText


testKey1 = "zyxwvutsrqponmlkjihgfedcba "
cipherText = "gsv jfrxp yildm ulc"
plainText = substitutionDecrypt(cipherText, testKey1)
print('CipherText:', cipherText)
print('PlainText:', plainText)

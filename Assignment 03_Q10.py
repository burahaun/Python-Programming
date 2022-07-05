str = input("Enter a string: ").lower()
def vowel(str):
    vowel = 0
    v = ["a","e","i","o","u"]
    for i in str:
        if i in v:
            vowel = vowel + 1
    return vowel
def consonant(str):
    v = ["a","e","i","o","u"]
    consonant = 0
    for i in str:
        if i not in v:
            consonant = consonant + 1
    return consonant

print("The string you entered includes",vowel(str),"vowels and",consonant(str),"consonants")

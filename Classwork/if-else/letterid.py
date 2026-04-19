ch = input("Enter a character: ").lower()

if ch.isalpha():
    if ch in 'aeiou':
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")
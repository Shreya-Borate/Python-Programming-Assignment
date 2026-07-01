#accept one character and checks it is vowel or consonant.

def ChkVowel(ch):
    vowels ="aeiou"
    Char = ch.lower()
    for c in ch:
        if c in vowels:
            return True

    
def main():
    c=input("Enter a Character : ")
    Ret = ChkVowel(c)

    if (Ret==True) :
        print("Vowel")
    else:
        print("Consonant ")

if __name__ =="__main__":
    main()
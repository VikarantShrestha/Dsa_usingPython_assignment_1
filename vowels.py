class Frequency:
    def countvowel(str):
        dict ={
            "a":0,
            "e":0,
            "i":0,
            "o":0,
            "u":0
        }

        vowel="aeiou"

        for c in str:
            if c in vowel:
                dict[c]+=1
        
        for c in vowel:
            if dict[c]>0:
                print(c ," : ",dict[c])


str=input("Enter string : ").lower()
ob=Frequency
ob.countvowel(str)
"""
CALLBACK Function example

eg: CALLBACK FUNCTION =
def isOdd(num):
    return (num % 2) != 0

MAIN FUNCTION =
def main((1,2,3,4,5), isOdd)

the CALLBACK fuction, isOdd is called for each val in the tuple. If any of the vals
is odd, return True

"""
#CallBack function
def callback_isVowel(char):
    return char in ("a","e","i","o","u")

def main(strin_g = "", _callback = None):
    print("Counting the number of vowels in {}".format(strin_g))
    vowel_ct = 0
    if _callback:
        for char in strin_g:
            if _callback(char):
                vowel_ct += 1
        print ("Result: {}".format(vowel_ct))

main("thisisawesome", callback_isVowel)
main("thisisnotveryawesome", callback_isVowel)

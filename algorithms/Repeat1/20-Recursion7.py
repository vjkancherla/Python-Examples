"""
Write a recursive function called isPalindrome which returns true if the string
passed to it is a palindrome (reads the same forward and backward).

eg: isPalindrome("awesome") // false
eg: isPalindrome("foobar") // false
eg: isPalindrome("amanaplanacanalpanama") // true
eg: isPalindrome("tacocat") // true
"""

def isPalindrome(str):
    def doWork(idx):
        if idx < 0:
            return ""

        return str[idx] + doWork(idx-1)

    rev_str = doWork(len(str)-1)

    if str == rev_str:
        print ("Palidrome = true")
    else:
        print ("Palidrome = false")



isPalindrome("awesome")
isPalindrome("foobar")
isPalindrome("amanaplanacanalpanama")
isPalindrome("tacocat")

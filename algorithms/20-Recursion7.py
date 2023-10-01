"""
Write a recursive function called isPalindrome which returns true if the string
passed to it is a palindrome (reads the same forward and backward).

eg: isPalindrome("awesome") // false
eg: isPalindrome("foobar") // false
eg: isPalindrome("amanaplanacanalpanama") // true
eg: isPalindrome("tacocat") // true
"""

def isPalindrome(str):
    start_idx = 0
    end_idx = len(str) - 1

    def doWork(str, start_idx, end_idx):
        if start_idx == end_idx:
            return True
        if str [start_idx] == str [end_idx]:
            start_idx += 1
            end_idx -= 1
        else:
            return False
        return doWork(str, start_idx, end_idx)

    return doWork(str, start_idx, end_idx)

print (isPalindrome("awesome"))
print (isPalindrome("foobar"))
print (isPalindrome("amanaplanacanalpanama"))
print (isPalindrome("tacocat"))

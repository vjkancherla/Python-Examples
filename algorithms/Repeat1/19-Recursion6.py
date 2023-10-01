"""
Write a recursive function called reverse which accepts a string
and returns a new string in reverse.

eg: reverse("awesome") // emosewa
eg: reverse("rythmschool") // loohcsmhtyr
"""

def reverse (strin_g):
    def doWork(idx):
        if idx < 0:
            return ""
        else:
            return strin_g [idx] + doWork(idx-1)

    rev_str = doWork(len(strin_g)-1)

    return "Reverse of '"+strin_g+"' is '"+rev_str+"''"

print(reverse("awesome"))
print(reverse("rythmschool"))

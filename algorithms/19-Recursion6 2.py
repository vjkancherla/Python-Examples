"""
Write a recursive function called reverse which accepts a string
and returns a new string in reverse.

eg: reverse("awesome") // emosewa
eg: reverse("rythmschool") // loohcsmhtyr
"""

def reverse(str):
    return doWork(str, len(str) - 1)

def doWork(str, str_idx):
    if str_idx < 0:
        return ""
    return str[str_idx] + doWork(str, str_idx-1)

print(reverse("awesome"))
print(reverse("rythmschool"))

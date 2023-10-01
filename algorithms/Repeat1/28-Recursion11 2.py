"""
Wite a function called nestedEvenSum. Return the sum of all even numbers in an
object which may contain nested objects.

eg: obj_1 = {
    "outer": 2,
    "obj_a": {
        "inner": 2,
        "obj_b": {
            "super_inner": 2,
            "not_a_number": True,
            "also_not_a_number": True
        }
    }
}

eg: obj_2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b":3, "bb": {"b":2}}},
    "c": {"c": {"c":2}, "cc":"ball", "ccc":5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"}
}

eg: obj_3 = {
    "obj_b": {
        "super_inner": 2,
        "not_a_number": True,
        "also_not_a_number": True
    }
}


nestedEvenSum(obj_1) //6
nestedEvenSum(obj_2) //10
nestedEvenSum(obj_3) //2
"""

even_sum = 0
print_line = True

def reset():
    global print_line
    global even_sum

    even_sum = 0
    print_line = True


def nestedEvenSum(dic_t):
    global print_line
    global even_sum

    if print_line:
        print("Processing {}".format(dic_t))
        print_line = False

    if len(dic_t) == 0:
        print ("The sum of all even numbers is the Dict is {}".format(even_sum))


    for key in dic_t:
        val = dic_t[key]
        if type(val) == int and val%2 == 0:
            even_sum += val
        elif type(val) == dict:
            nestedEvenSum(val)

obj_1 = {
    "outer": 2,
    "obj_a": {
        "inner": 2,
        "obj_b": {
            "super_inner": 2,
            "not_a_number": True,
            "also_not_a_number": True
        }
    }
}

obj_2 = {
    "a": 2,
    "b": {"b": 2, "bb": {"b":3, "bb": {"b":2}}},
    "c": {"c": {"c":2}, "cc":"ball", "ccc":5},
    "d": 1,
    "e": {"e": {"e": 2}, "ee": "car"}
}

obj_3 = {
    "obj_b": {
        "super_inner": 2,
        "not_a_number": True,
        "also_not_a_number": True
    }
}

nestedEvenSum(obj_1)
print ("EvenSum={}".format(even_sum))
reset()
nestedEvenSum(obj_2)
print ("EvenSum={}".format(even_sum))
reset()
nestedEvenSum(obj_3)
print ("EvenSum={}".format(even_sum))
reset()

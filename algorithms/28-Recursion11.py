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

def nestedEvenSum(dic_t):
    print ("Processing: {}".format(dic_t))

    # an Int can't be updated within the inner function, hence using a list as a workaround
    even_count = [0]
    def doWork(dic_t, even_count):
        if len(dic_t) == 0:
            even_count [0] = even_count [0] + 0
            return even_count

        for dict_item in dic_t:
            dict_item_val = dic_t [dict_item];

            #print ("->dict_item={}\n->dict_item_val={}".format(dict_item,dict_item_val))

            if (type(dict_item_val) == int) and (dict_item_val%2 == 0):
                even_count [0] = even_count [0] + dict_item_val
                continue
            elif type(dict_item_val) == dict:
                doWork(dict_item_val, even_count)

    doWork(dic_t, even_count)

    print ("The Even Count is {}".format(even_count))


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
nestedEvenSum(obj_2)
nestedEvenSum(obj_3)

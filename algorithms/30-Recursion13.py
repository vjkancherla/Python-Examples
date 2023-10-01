"""
Write a function called stringifyNumbers which takes an object and finds all the values
which are number and converts them to string

eg: obj_1 = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
        }
    }
}

//result should be:
obj_1 = {
    "num": "1",
    "test": [],
    "data": {
        "val": "4",
        "info": {
            "isRight": True,
            "random": "66"
        }
    }
}
"""

def stringifyNumbers(dic_t):
    print ("Processing: {}".format(dic_t))

    def doWork(dic_t):
        if len(dic_t) == 0:
            return

        for dict_key in dic_t:
            val = dic_t [dict_key]

            if type(val) == int:
                dic_t [dict_key] = str(val)
                continue
            elif type(val) == dict:
                 doWork(val)

    doWork(dic_t)

    print ("Result = {}".format(dic_t))


obj_1 = {
    "num": 1,
    "test": [],
    "data": {
        "val": 4,
        "info": {
            "isRight": True,
            "random": 66
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

stringifyNumbers(obj_1)
stringifyNumbers(obj_2)

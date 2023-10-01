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

def stringifyNumbers(objec_t):
    print ("Processing Object:{}".format(objec_t))

    def doWork(objec_t):

        if len(objec_t) == 0:
            return

        for key in objec_t:
            val = objec_t[key]
            if type(val) == int:
                objec_t[key] = str(val)
            elif type(val) == dict:
                doWork(val)

    doWork(objec_t)

    print("Result: {}".format(objec_t))

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

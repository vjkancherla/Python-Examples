"""
Write a function called collectStrings, which accepts an object and returns an array of
all the values in the object that have a "typeOf" string.

eg: obj_1 = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": "baz"
                    }
                }
            }
        }
    }
}

// returns ["foo", "bar", "baz"]
"""

def collectStrings(objec_t):
    print ("Processing Object: {}".format(objec_t))

    str_collection = []
    def doWork(objec_t):
        if len(objec_t) == 0:
            return

        for key in objec_t:
            val = objec_t [key]
            if type(val) == str:
                str_collection.append(val)
            elif type(val) == dict:
                doWork(val)

    doWork(objec_t)

    print ("Result : {}".format(str_collection))


obj_1 = {
    "stuff": "foo",
    "data": {
        "val": {
            "thing": {
                "info": "bar",
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": "baz"
                    }
                }
            }
        }
    }
}

obj_2 = {'a': '2', 'c': {'cc': 'ball', 'c': {'c': '2'}, 'ccc': '5'}, 'b': {'b': '2', 'bb': {'b': '3', 'bb': {'b': '2'}}}, 'e': {'ee': 'car', 'e': {'e': '2'}}, 'd': '1'}

collectStrings(obj_1)
collectStrings(obj_2)

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

def collectStrings(dic_t):
    print ("Processing: {}".format(dic_t))

    strings_list = []
    def doWork(dic_t):
        if len(dic_t) == 0:
            return

        for dict_key in dic_t:
            val = dic_t [dict_key]

            if type(val) == str:
                strings_list.append(val)
                continue
            elif type(val) == dict:
                doWork(val)

    doWork(dic_t)

    print ("Result: {}".format(strings_list))


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

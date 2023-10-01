#!/usr/bin/env python3
import random
aList = random.sample(range(1, 100), 10)
bList = random.sample(range(1, 100), 10)

commonSet = set()

for i in aList:
    if i in bList:
        commonSet.add(i)

print ("{a} intersetion {b} = {c}".format(a=aList, b=bList, c=commonSet))

#An even simpler way
setA = set(aList)
setB = set(bList)
commonSet = setA & setB
print ("{}".format(commonSet))

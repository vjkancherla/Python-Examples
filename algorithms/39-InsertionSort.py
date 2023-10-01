"""
INSERTION SORT::
the insertion sort, although still O(n2), works in a slightly different way. It always maintains
a sorted sublist in the lower positions of the list. Each new item is then "inserted" back into
the previous sublist such that the sorted sublist is one item larger.
On each pass, one for each item 1 through n-1, the current item is checked against those in the
already sorted sublist. As we look back into the already sorted sublist, we shift those items that
are greater to the right. When we reach a smaller item or the end of the sublist, the current item
can be inserted.

===
mark first element as sorted

for each unsorted element X

  'extract' the element X

  for j = lastSortedIndex down to 0

    if current element j > X

      move sorted element to the right by 1

    break loop and insert X here
===

https://visualgo.net/en/sorting
"""

def insertionSort(lis_t):
    print ("Processing {} for sorting".format(lis_t))

    for i in range(1, len(lis_t)):

        val = lis_t [i]

        print("Val_to_insert:{} in sorted_part:{}".format(val, lis_t[:i]))

        if val < lis_t[i-1]:
            # go backwards, eg: 4,3,1,0
            # similar to for(i=3;i>-1;i--)
            for j in range(i-1, -1, -1):
                if val < lis_t [j]:
                    lis_t [j+1] = lis_t [j]
                else:
                    lis_t [j+1] = val
                    break

        print ("Sorted_part2:{}".format(lis_t[:i+1]))
        print ("---")

    print ("Result: {}".format(lis_t))

insertionSort([3,44,38,5,47,15,36,26,27,2])
#insertionSort([3,44,38,5,47,15,36,26,27,2,46,4,19,50,48])

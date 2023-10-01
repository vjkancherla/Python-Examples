'''
Write a function to implement Bubble Sorting.

With Bubble Sort, the bigger numbers "bubble to the top" (to the end of the array/list)

we are going along the entire array and compare every 2 neighboring elements.
If they are in the wrong order (the left neighbor is bigger than the right one),
we swap them. At the first pass at the end it will appear the biggest element
(if we sort in ascending order). You may say, the biggest element “pops up”.
That’s the reason of the Bubble sort algorithm name.

We repeat the first step from the first to the next-to-last element.
We’ve got the second biggest element at the next-to-last place. And so on.
We can improve an algorithm a little bit with checking out if at least one exchange
at the previous step was made. If it isn’t we stop our running along the array.

First Pass:
( 5 1 4 2 8 ) –> ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 ) –>  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 ) –>  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 ) –> ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.

// Visaulise the algorithm
https://visualgo.net/en/sorting?slide=1

Big O: n^2

'''
#[3,1,45,53,2,32,1]
# def doBubbleSort(lis_t):
#     print ("About to Bubble Sort {}".format(lis_t))
#
#     start_idx = 0
#     end_idx   = len(lis_t) - 1
#
#     while end_idx >= 0:
#         val_1 = lis_t [start_idx]
#         val_2 = lis_t [start_idx + 1]
#
#         if val_1 > val_2:
#             #Swap
#             lis_t [start_idx] = (val_1 + val_2) - val_1
#             lis_t [start_idx+1] = (val_1 + val_2) - val_2
#
#         start_idx += 1
#
#         #end of an iteration. Restart
#         if start_idx > end_idx-1:
#             start_idx = 0
#             end_idx -= 1
#
#     print ("Result: {}".format(lis_t))

def doBubbleSort(lis_t):
     print ("About to Bubble Sort {}".format(lis_t))

     # iterate backwards.
     # For eg: range(10, 0, -1), which gives
     # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
     for i in range(len(lis_t)-1, 0, -1):
         # After every iteration, the last element will be the largest.
         # So, we need to sort n-1 vals in the next iteration

         no_swaps = True

         for j in range(i):
             val_1 = lis_t [j]
             val_2 = lis_t [j + 1]

             if val_1 > val_2:
                 #Swap
                 lis_t [j] = (val_1 + val_2) - val_1
                 lis_t [j+1] = (val_1 + val_2) - val_2
                 no_swaps = False

         # If there were NO swaps during the above iteration
         # then all swapping is done. Break out
         # Otherwise, we will try to swap items that have
         # already been swapped/sorted
         if no_swaps:
            break

     print("Result: {}".format(lis_t))



doBubbleSort([3,1,45,53,2,32,1])
doBubbleSort([323,43,6,444,2,33,11,45,23])
doBubbleSort([5,1,2,3,4,5,6,7,8])

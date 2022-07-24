"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""
import copy

def binary_search(input_array, value):
    """Your code goes here."""
    search_array = copy.copy(input_array)
    while True:
        middleElem = search_array[len(search_array) // 2]
        middleElemIndex = len(search_array) // 2
        if middleElem == value:
            return input_array.index(middleElem)
        if len(search_array) == 1:
            break
        if value > middleElem:
            search_array = search_array[middleElemIndex + 1:]
            continue
        if value < middleElem:
            search_array = search_array[:middleElemIndex]
            continue
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print (binary_search(test_list, test_val1))
print (binary_search(test_list, test_val2))

#Binary Search time complexity O(log(n))
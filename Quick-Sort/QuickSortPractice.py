def partition(list, left, right):
    x = list[right]
    i = left
    for j in range(left, right):
        if list[j] <= x:
            swap = list[i]
            list[i] = list[j]
            list[j] = swap
            i += 1
    swap = list[i]
    list[i] = list[right]
    list[right] = swap
    return i 

def quickSorting(list, left, right):
    if left < right:
        pivot = partition(list, left, right)
        quickSorting(list, left, pivot - 1)
        quickSorting(list, pivot + 1, right)

def quickSort(list):
    quickSorting(list, 0, len(list) - 1)



list = [i for i in range(100)]
list = list[::-1]
print(f'Before Sorting: {list}')
quickSort(list)
print(f'After Sorting: {list}')


# Best and Average time complexity O(nlog(n))
# Worst time complexity O(n^2)
# Space complexity O(1)
def bubbleSort(list):
    n = len(list)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if list[i - 1] > list[i]:
                temp = list[i]
                list[i] = list[i - 1]
                list[i - 1] = temp
                swapped = True



list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print('Before sorting: ', end='')
print(list)
bubbleSort(list)
print('After sorting: ', end='')
print(list)

# Best time complexity O(n)
# Worst and Average time complexity O(n^2)
# Space complexity O(1) because of sorting in place
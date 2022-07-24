import sys
def merge(list, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid
    L = [i for i in range(n1 + 1)]
    R = [i for i in range(n2 + 1)]
    for i in range(n1):
        L[i] = list[left + i]
    for j in range(n2):
        R[j] = list[mid + j + 1]
    L[n1] = sys.maxsize
    R[n2] = sys.maxsize
    i = 0
    j = 0
    for k in range(left, right + 1):
        if L[i] <= R[j]:
            list[k] = L[i]
            i += 1
        else:
            list[k] = R[j]
            j += 1

def mergeSorting(list, left, right):
    if left < right:
        mid = (left + right) // 2
        mergeSorting(list, left, mid)
        mergeSorting(list, mid + 1, right)
        merge(list, left, mid, right)


def mergeSort(list):
    mergeSorting(list, 0, len(list) - 1)

 

list = [i for i in range(11)]
list = list[::-1]
print('Before sorting: ', end='')
print(list)
mergeSort(list)
print('After sorting: ', end='')
print(list)

#time complexity O(nlog(n)) = Best and Average and Worst
#Space complexity = O(n)
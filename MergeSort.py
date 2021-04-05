def mergeSort(List):
    if len(List) == 1:
        return List
    mid = len(List) // 2
    left = List[:mid]
    right = List[mid:]
    return mergeSort_c(mergeSort(left), mergeSort(right))

def mergeSort_c(left, right):
    List = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            List.append(left.pop(0))
        else:
            List.append(right.pop(0))
    List += right
    List += left
    return List

print(mergeSort([1, 3, 2, 4, 2, 3, 3]))

a = [1, 2, 3]
def ls(a):
    a.append(1)
    print(a)
ls(a)
print(a)


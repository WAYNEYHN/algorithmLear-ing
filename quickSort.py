def quickSort(List, left, right):
    if left >= right:
        return List
    mid = getmid(List, left, right)
    quickSort(List, left, mid - 1)
    quickSort(List, mid + 1, right)
    return List


def getmid(List, left, right):
    value = List[right]
    i = left
    for j in range(left, right):
        if List[j] < value:
            List[i], List[j] = List[j], List[i]
            i += 1
    List[i], List[right] = List[right], List[i]
    return i


print(quickSort([1, 2, 0, 4, 0], 0, 4))

# a = ['a', 'b', 'c', 'd', 'a', 'e', 'f']

import re

# re.findall('^(25[0-5])|(2[0-4]\d)|([01]?\d\d?)(\.(25[0-5])|(2[0-4]\d)\([01]?\d\d?){3}$')
# print(re.match('^(25[0-5])|(2[0-4]\d)|([01]?\d\d?)(\.(25[0-5])|(2[0-4]\d)\([01]?\d\d?){3}$', "127.127.124.124"))
str = "****c**sdsf***"
#
# for i in str:
#     if i != '*':
#
# str.split()
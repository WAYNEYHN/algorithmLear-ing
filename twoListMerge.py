def mergeSorted(l1, l2):
    return mergeSorted_1(l1, l2, [])
def mergeSorted_1(l1, l2, tmp):
    if l1 is None or l2 is None:
        tmp.extend(l1)
        tmp.extend(l2)
        return tmp
    else:
        if l1[0] < l2[0]:
            tmp.append(l1[0])
            del l1[0]
        else:
            tmp.append(l2[0])
            del l2[0]
        return mergeSorted_1(l1, l2, tmp)


def Merge(l1, l2):
    ans = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            ans.append(l1.pop(0))
        else:
            ans.append(l2.pop(0))
    ans.extend(l1)
    ans.extend(l2)
    return ans

print(Merge([1, 3, 5], [2, 4, 6]))
def selectSort(nums):
    Len = len(nums)
    for i in range(Len - 1):
        Min = i
        for j in range(i + 1, Len):
            if nums[j] < nums[Min]:
                Min = j
        nums[Min], nums[i] = nums[i], nums[Min]

    return nums


def bubbleSort(nums):
    Len = len(nums)
    flag = False
    for i in range(Len - 1):
        for j in range(Len - i - 1):
            if (nums[j] > nums[j + 1]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                flag = True

        if not flag: break
    return nums


def insertSort(nums):
    Len = len(nums)
    for i in range(1, Len):
        flag = i - 1
        value = nums[i]
        while value < nums[flag] and flag >= 0:
            nums[flag + 1] = nums[flag]
            flag -= 1
        nums[flag + 1] = value
    return nums


def mergeSort(nums):
    if len(nums) == 1: return nums
    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]
    return merge(mergeSort(left), mergeSort(right))


# from heapq import merge
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result += left
    result += right
    return result


def quickSort(nums, left, right):
    if left >= right:
        return nums
    k = Partitions(nums, left, right)
    quickSort(nums, left, k-1)
    quickSort(nums, k+1, right)
    return nums

def Partitions(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    print(i)
    nums[i], nums[right] = nums[right], nums[i]
    return i


print(quickSort([1,2,0,4,0], 0, 4))
# print(quickSort([2, 3, 7, 1, 0, 9, 5, 0], 0, 7))


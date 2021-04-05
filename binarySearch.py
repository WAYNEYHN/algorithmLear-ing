def BinarySearch(List, target):
    length = len(List)
    left = 0
    right = length-1
    while left <= right:
        mid = (right - left) // 2 + left
        if target > List[mid]:
            left = mid + 1
        elif target < List[mid]:
            right = mid - 1
        else:
            #如果进行二分查找的列表含有重复元素
            while mid != 0 and nums[mid-1] == nums[mid]:
                mid -= 1
            return mid
    return None



print(BinarySearch([1,1,2,3,7,7,7,9,9,10],2))
class Solution:
    def more_than_half(self, nums):
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = 1
            else:
                dict[num] += 1
                if  dict[num] > len(nums)/2:
                    return num
        return 0
import re


class Solution:
    def twoSum(self, nums, target):
        dict = {}
        for i, m in enumerate(nums):
            if dict.get(target - m) is not None:
                return [dict.get(target-m), i]
            dict[m] = i
# l = [1, 2, [1, 2]]
# a = l
# b = l[:]
# l.append(4)
# l[2].append(3)
# print(l)
# print(a)
# print(b)
def minPathSum(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i==0 and j==0:
                continue
            elif i==0:
                grid[i][j] = grid[i][j-1] + grid[i][j]
            elif j==0:
                grid[i][j] = grid[i-1][j] + grid[i][j]
            else:
                grid[i][j] = min(grid[i-1][j], grid[i][j-1])+ grid[i][j]
    return grid[-1][-1]

a = {"yagn":1, "hao":2, "nan":3}
for x in a:
    print(x)

def keys(**k):
    pass

# keys("xx")
# keys({"names":"123", "ynag":"12"})
# keys(name="xx")
n = int(input())

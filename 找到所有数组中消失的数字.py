'''
给你一个含n个整数的数组nums，其中nums[i]在区间[1, n]内。请你找出所有在[1, n] 范围内但没有出现在nums中的数字，并以数组的形式返回结果。
例如： 输入：nums = [4,3,2,7,8,2,3,1]  输出：[5,6]
'''

nums = [4,3,2,7,8,2,3,1]
result = []
for i in range(1, len(nums)):
    if i not in nums:
        result.append(i)
print(result)
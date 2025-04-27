'''
给你一个长度为n的整数数组nums ，其中nums的所有整数都在范围[1,n]内，且每个整数出现最多两次。请你找出所有出现两次的整数，并以数组形式返回。
例如： 输入：nums = [4,3,2,7,8,2,3,1] 输出：[2,3]
'''

nums = [4,3,2,7,8,2,3,1]
result = []
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[j] == nums[i]:
            result.append(nums[j])
print(result)
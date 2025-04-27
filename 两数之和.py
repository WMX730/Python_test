'''
给定一个整数数组nums和一个整数目标值 target，请你在该数组中找出 和为目标值target的那两个整数，并返回它们的数组下标。
例如：输入：nums = [2,7,11,15], target = 9 输出：[0,1]
'''

nums = [15,7,11,2]
target = 9
dict_index = {}

for i in range(len(nums)):
    num = nums[i]
    a = target - num
    if a in dict_index:
        print([dict_index[a], i])
    dict_index[num] = i




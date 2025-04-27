'''
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置
例如：  输入: nums = [1,3,5,6], target = 5  输出: 2
'''

nums = [1,3,5,6]
target = 2
if target in nums:
    for i in range(len(nums)):
        if nums[i] == target:
            print(i)
else:
    target = [target]
    new_num = nums + target
    new_nums = sorted(new_num)
    print(new_nums)

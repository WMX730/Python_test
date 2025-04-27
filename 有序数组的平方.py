'''
给你一个按非递减顺序排序的整数数组nums，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
例如： 输入：nums = [-4,-1,0,3,10] 输出：[0,1,9,16,100]
'''

nums = [-4,-1,0,3,10]
new_nums = []
for i in nums:
    new_nums.append(i*i)
result = sorted(new_nums)
print(result)

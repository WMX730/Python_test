'''
给你一个整数数组nums，返回数组answer，其中answer[i]等于nums中除nums[i]之外其余各元素的乘积 。
题目数据保证数组nums之中任意元素的全部前缀元素和后缀的乘积都在 32位整数范围内。
例如： 输入: nums = [1,2,3,4] 输出: [24,12,8,6]
'''

nums = [1,2,3,4]
answer = [1] * len(nums)
a = 1
for i in range(len(nums)):
    answer[i] = a
    a *= nums[i]
print(answer)
b = 1
for j in range(len(nums)-1,-1,-1):
    print(j, answer[j])
    answer[j] *= b
    b *= nums[j]
print(answer)

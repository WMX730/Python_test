'''
给你一个整型数组nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积
例如： 输入：nums = [1,2,3,4] 输出：24
'''

nums = [1,2,3]
first = second = third = min(nums)
for num in nums:
    if num > first:
        third = second
        second = first
        first = num
    else:
        if num > second:
            third = second
            second = num
        else:
            third = num
result = first * second * third
print(result)





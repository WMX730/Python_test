'''
给你一个非严格递增排列的数组nums，请你原地删除重复出现的元素，使每个元素只出现一次，返回删除后数组的新长度。
元素的相对顺序应该保持一致 。然后返回 ums中唯一元素的个数。
例如：  输入：nums = [0,0,1,1,1,2,2,3,3,4] 输出：5, nums = [0,1,2,3,4]
'''


nums = [0,0,1,1,1,2,2,3,3,4]
new_num = []
for i in nums:
    if i in new_num:
        pass
    else:
        new_num.append(i)

print("数组长度：", len(new_num), "nums:", new_num)


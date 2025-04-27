'''
给你一个数组nums和一个值val，你需要原地移除所有数值等于val的元素。元素的顺序可能发生改变。然后返回nums中与val不同的元素的数量。
例如： 输入：nums = [3,2,2,3], val = 3 输出：2, nums = [2,2,_,_]
'''

nums = [3,2,2,3]
val = 3
num_new = []
for i in nums:
    if i != val:
        num_new.append(i)
print(len(num_new), num_new)
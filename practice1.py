'''
if for while break continue 混合练习
'''
# # task1：打印所有大于0且是奇数的数字
# nums = [4, -3, 7, 0, 2, -1, 9, -5]
# for i in nums:
#     if i > 0 and i % 2 != 0:
#         print(i)

# task2:从1加到100，遇到能被7整除的就停止
sum = 0
for i in range(1,100):
    sum += i
    if sum % 7 == 0:
        print("i:", i,"当前和:", sum)
        break
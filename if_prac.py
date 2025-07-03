'''
if条件判断
'''

'''
如果只有两种情况,最好用if else
用if if,会各自执行判断,降低效率
'''
# # if else
# x = 0  # x的取值只有0和1时
# if x == 0:
#     print("success")
# else:
#     print("fail")

# # if if 
# if x == 0:
#     print("success")    
# if x == 1:
#     print("fail")

'''
如果有多种情况:
    使用if if if 会导致满足多个情况
    使用if elif else 可以避免这种情况
    但如果有多个elif, 需要注意顺序, 先满足的条件
'''
a = 5
if a > 0:
    print("大于0")
if a < 10:
    print("小于10")
else:
    print("不小于10")
# 会同时输出：大于0、小于10

if a > 10:
    print("大于10")
elif a > 0:
    print("大于0")
else:
    print("介于0和10之间")
# 只会输出：大于0


'''
列表推导式
[表达式 for 变量 in 可迭代对象]
    [i for i in data]             复制一份data
    [f(i) for i in data]          把每个元素用f()函数处理一遍
    [i for i in data if 条件]     筛选满足条件的元素
    [f(i) for i in data if 条件]  先筛选，再加工

'''

# 复制元素
a = [1, 2, 3, 4, 5]
b = a      # 只是引用了同一个对象（地址），并没有真的“复制”数据
b[0] = 100
print(a)   # b改变a也会跟着改变  [100, 2, 3, 4, 5] 
c = [i for i in a]
print(c)   # 真正复制了数据，c和a是两个独立的列表
c[0] = 200
print(a)   # a不受c的影响，仍然是 [100, 2, 3, 4, 5]
print(c)   # c变成了 [200, 2, 3, 4, 5]


# # 加工元素
# squared = [x ** 2 for x in range(5)]   # [0, 1, 4, 9, 16]

# squared = []
# for x in range(5):
#     s = x ** 2
#     squared.append(s)



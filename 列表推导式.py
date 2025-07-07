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

# 加工元素
squared = [x ** 2 for x in range(5)]   # [0, 1, 4, 9, 16]  不用提前定义squared = []

squared = []
for x in range(5):
    s = x ** 2
    squared.append(s)

def square(x):
    return x ** 2
data = [square(i) for i in range(5)]  

# 筛选元素
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# 加工 + 筛选
processed = [x*10 for x in range(10) if x % 2 == 0]  # [0, 20, 40, 60, 80]


# practice 
data1 = [i for i in range(10)]
print(data1)  

def square(x):
    return x ** 2
data2 = [square(i) for i in range(9)]
print(data2)

list1 = list(range(1,8))
data3 = [i for i in list1 if i % 2 == 0]
print(data3)  

list2 = [ 1, 2, 3, 4, 5]
data4 = [i * 10 for i in list2]
print(data4)  

nums = [1, -3, 5, -10, 7, -2]
def square(x):
    return x ** 2
data5 = [square(i) for i in nums if i > 0]
print(data5)  

# 字母大小写转换函数： s.lower()把字符串s全部转为小写 // s.upper()把字符串s全部转为大写
s = "HelloWorld"
data6 = [i.lower() for i in s]
print(data6)  

names = ["Alice", "Bob", "Charlie"]
scores = [80, 65, 90]
zipped = zip(names, scores)
result = [f"{name}:{score}" for name,score in zipped]

result = []
for i in range(1,4):
    for j in range(1,3):
        result.append((i, j))
print(result)  
data8 = [(x,y) for x in range(1,4) for y in range(1,3)]

prac1 = [i for i in range(1,21) if i % 2 == 0]
print(prac1) 

exmple = [3, 6, 9, 12]
prac2 = [i-1 for i in exmple]
print(prac2)  

nums = [-5, 2, 0, 8, -3, 7]
prac3 = [str(i) for i in nums if i >0]
print(prac3)

# 判断是不是字母 ch.isalpha()   //   大小写互换 ch.swapcase()
s = "a1B2c3D4"
result = [ch.swapcase() for ch in s if ch.isalpha()]
print(result)
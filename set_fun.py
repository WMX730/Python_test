'''
    set() 函数:去重
'''

# set() 函数创建一个无序不重复元素集，基本功能是去重
data1 = set()
data1.add(1)
data1.add(2)
data1.add(2)
print(data1)  

# 对已有的数据集进行去重
data2 = (1,1,2,3,4,4,5,6,6,6,7,8)
data2 = set(data2)
print(data2)
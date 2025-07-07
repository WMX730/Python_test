'''
访问属性：“.”  “[]"
'''

'''   []访问   '''
# 字典
dic = {"k1": "v1",
       "k2": "v2",
       "k3": "v3"}
data = dic["k1"]
# 列表
list = [1, 2, 3, 4, 5]
data = list[0]
# 字符串
str = "hello world"
data = str[0]
 
'''   .访问   '''
# 类
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
person = Person("张三", 20)
data = person.name
data1 = person.greet()
print(data1)
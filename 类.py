'''
class类  面向对象
'''

class Myclass:
    def __init__(self, i, j):  # 构造函数（初始化）
        self.i = i    # 实列变量
        self.j = j

    i = 123456   # 类变量（属性）

    def f(self): # 方法
        return 'Hello world!'

x = Myclass(1, 2)   # 创建对象时会自动调用__init__方法
# print(x.i, x.j)

x.y = 200
print(x.y)

a = x.f()   # 是一个object对象
b = Myclass.f(x)  # 是一个函数，必须有一个self的输入
print(a)
print(b)

class Person:
    nation = "China"    # 属性

    def __init__(self, name, age):  # 初始化，每次使用类创建新对象时都会自动调用该函数
        # 将值赋给对象属性
        self.name = name
        self.age = age
        # self参数是对类的当前实例的引用，用于访问属于该类的变量

    def get_nation(self):
        print(self.nation)

p1 = Person("Bill", 63)
print(p1.name)
print(p1.age)
print(p1.nation)
p1.get_nation()
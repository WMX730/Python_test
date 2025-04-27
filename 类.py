'''
class类  面向对象
'''

class Myclass:
    def __init__(self, i, j):  # 初始化
        self.i = i
        self.j = j

    i = 123456   # (属性)

    def f(self): #（方法）
        return 'Hello world!'

x = Myclass(1, 2)
# print(x.i, x.j)

x.y = 200
print(x.y)

a = x.f()   # 是一个object对象
b = Myclass.f(x)  # 是一个函数，必须有一个self的输入
print(a)
print(b)
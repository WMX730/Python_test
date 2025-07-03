'''
*args、**kwargs是python函数种用于接收任意数量参数的用法
  *args表示接收任意数量的位置参数（以元组的形式传入）
  **kwargs表示接收任意数量的关键字参数（以字典的形式传入）
位置参数：按顺序传值
关键字参数：指定参数名来传值
混合使用（位置参数必须在关键字参数前）
'''

def add_all(*args):
    print(args)  
    return sum(args)

print(add_all(1, 2, 3))       
print(add_all(10, 20, 30, 40)) 

def print_info(**kwargs):
    print(kwargs)  
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, job="Engineer")

def example(*args, **kwargs):
    for arg in args:
        print(arg)
    # print("args:", args)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    # print("kwargs:", kwargs)

# example(1, 2, 3, name="Tom", city="Beijing")

nums = [1, 2, 3]
info = {'name': 'Alice', 'age': 30}
example(*nums, **info)


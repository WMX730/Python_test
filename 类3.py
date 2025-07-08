'''
类继承

class 父类名：
    # 父类中的属性和方法

class 子类名(父类名):
    # 子类中新增或重写的属性和方法
'''

# demo
class Animal:
    def speak(self):
        print("动物在叫")
class Dog(Animal):
    def speak(self):
        print("狗在叫")
d = Dog()
d.speak()  

'''
1、子类继承父类的方法和属性：即使在子类中没有定义，python也会自动查找父类中的方法和属性。
2、子类可以重写父类的方法：子类可以定义与父类同名的方法，这样就会覆盖父类中的方法。
   可以使用super()函数调用父类的方法。
3、子类可以添加新的属性和方法：子类可以在父类的基础上添加新的属性和方法。
4、构造函数继承(__init__)
'''

# 构造函数继承demo
class Animal:
    def __init__(self, name):
        self.name = name
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # 调用父类的构造函数
        self.breed = breed      # 添加新的属性



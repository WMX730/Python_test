'''
类属性
    公有属性：没有加下划线的属性
    私有属性：加了一个下划线的属性(_)(外部还是可以访问的)，类似一个约定，告诉开发者这个属性是“内部的”
             加了两个下划线的属性(__)(外部是不能访问的)，只能通过 _ClassName__attribute访问
'''


# # 类
class Person:
    __data = "不能访问的私有数据"
    _internal_data = "私有数据"  # 私有属性
    public_data = "公有数据"    # 公有属性
    def __init__(self, name, age): # 构造函数，创建对象时会自动调用
        self.name = name # 属性
        self.age = age   # 属性

    def say_hello(self):  # 方法
        print(f"你好，我叫{self.name}，今年{self.age}岁")

p1 = Person("小明", 18)  # 创建一个对象
p1.say_hello()           # 调用对象的方法
print(p1.name)                  # 访问对象的属性
print(p1.public_data)
print(p1._internal_data) 
# print(p1.__data)       # 访问会报错
print(p1._Person__data)  # 正确访问私有属性的方式
 



# # 继承（子类）
# class Student(Person):  # 继承Person类
#    def study(self):
#        print(f"{self.name}正在学习")


# s = Student("小红", 20)  
# s.say_hello()           # 调用父类的方法
# s.study()               # 调用子类的方法



# # @classmethod使用
# '''
# @classmethod
# def 方法名(cls):
# '''
# class Book:
#     category = "小说"  # 类属性

#     def __init__(self,title):
#         self.title = title
    
#     def print_title(self):
#         print(f"书名：{self.title}")
#         print(f"类别：{self.category}")  # 访问类属性

#     @classmethod
#     def print_category(cls,new_category):  # 类方法
#         # print(f"类别：{cls.category}")  # cls代表类本身，可以访问类属性和类方法
#         cls.category = new_category  # 修改类属性

# b = Book("三体")
# b.print_title()  
# b.category = "科幻小说"  #只能在外部修改实例属性，不能修改类属性
# print(b.category)
# Book.print_category("科幻小说")  
# print(b.category)

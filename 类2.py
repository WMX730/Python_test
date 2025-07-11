'''
类方法 @classmethod
'''

class User:
    default_role = "普通用户"
    def __init__(self, name, role=None):
        self.name = name
        self.role = role or self.__class__.default_role

    def show_info(self):
        print(f"我是 {self.name}，我的角色是：{self.role}")

    @classmethod
    def create_admin(cls, name):
        return cls(name, role="管理员")

    @classmethod
    def create_guest(cls, name):
        return cls(name, role="访客")

    @classmethod
    def create_user(cls, name):
        return cls(name)
    
    @classmethod
    def set_default_role(cls, new_role):
        cls.default_role = new_role

U1 = User.create_user("小明")
U2 = User.create_admin("小红")
U3 = User.create_guest("游客001")

U1.show_info()
U2.show_info()
U3.show_info()

User.set_default_role("测试用户")   # 利用@classmethod修改类属性
U4 = User.create_user("小白")
U4.show_info()

class Person:
    nation = "China"

    @classmethod
    def get_nation(cls):  # cls 指的是类本身
        print(f"国籍是：{cls.nation}")

# 不用创建对象，直接用类调用
Person.get_nation()  # 输出：国籍是：China


# 与单纯的类对比
class Person:
    species = "Human"

    def __init__(self, name):
        self.name = name

    def say_hello(self):  # 普通实例方法
        print(f"Hi, I'm {self.name}")  # 这里用 self

    @classmethod
    def get_species(cls):  # 类方法
        print(f"We are {cls.species}")  # 这里用 cls，不能用 self

p = Person("亲")
p.say_hello()         # 输出：Hi, I'm 亲
Person.get_species()  # 输出：We are Human

class Person:
    species = "Human"  # 类变量，属于类

    def __init__(self, name):
        self.name = name  # 实例变量，属于对象

    @classmethod
    def get_species(cls):
        print(cls.species)  # 可以访问类变量

    @classmethod
    def create_and_hello(cls, name):
        person = cls(name)   # 可以用 cls 创建对象
        print(f"Hello, {person.name}")  # 访问对象属性




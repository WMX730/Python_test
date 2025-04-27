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
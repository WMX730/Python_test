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

def add(a, b):
    sum = a + b
    print(sum)
    def test():
        print("这是内层函数")
    test()
add(10, 20)

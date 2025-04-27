# 迭代器 iter  节省空间
s = 'abcd'
it = iter(s)
for i in range(len(s)):
    print(next(it))

# 生成器
# 方式1：元组推导式
gen_1 = (i *2 for i in range(5))
for i in gen_1:
    print(i)
print(next(gen_1))

# 方式2：yield
def gen_func():
    for x in range(5):
        yield x*x
f = gen_func()
for i in range(5):
    print(next(f))
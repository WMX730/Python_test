'''
dic字典
'''

dict ={"name": "Alice",
        "age": 25, 
        "city": "Beijing"}

# .item()返回一个包含(key,value)的可迭代对象
for a, b in dict.items():
    print(a)
    print(b)

print("==========")

for k in dict.keys():    # .keys()返回所有的key
    print(k)
for v in dict.values():  # .values()返回所有的value
    print(v)


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

for k in dict.keys():
    print(k)
for v in dict.values():
    print(v)


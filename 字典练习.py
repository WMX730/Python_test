from time import process_time_ns

dic = {
    "k1": "v1",
    "k2": "v2",
    "k3": [11, 22, 33],
    "k4" : {"a1": [1,2,3],
            "b1": 2
            },
    "k5":{"a2": [4,5,6],
          "b1": 8
    }
}
# for i in dic.keys():    
#     print(i)
# for j in dic.values():
#     print(j)

# for k,v in dic.items():
#     print(k,v)

# print(dic.keys())   
# print(dic.values())
# print(dic.items())

# dic['k4']['a1'].append(44)
# print(dic)
# print("====================")

# x = {}
# y = x
# x['key'] = "value"
# x = {}
# print(y)
# print("====================")
# x.clear()
# print(y)
# print("====================")

# student = {'小智': '1002', 'info':['小张','1006','man']}
# st = student.copy()
# print(st)
# st['小智']='1005'
# print(st)
# print(student)
# st['info'].remove('man')
# print(st)
# print(student)

name = ["小明", "小红", "小刚", "小丽", "小张", "小李"]
age = [18, 19, 20, 21, 22, 23]
student = {}
for i in range(len(name)):
    student[name[i]] = age[i]
print(student)
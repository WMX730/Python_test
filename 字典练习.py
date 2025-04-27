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
#     print("====================")
# for j in dic.values():
#     print(j)
#     print("====================")
#
# for k,v in dic.items():
#     print(k,v)
#     print("====================")
#
# dic['k4']['a1'].append(44)
# print(dic)
# print("====================")

x = {}
y = x
x['key'] = "value"
x = {}
print(y)
print("====================")
x.clear()
print(y)
print("====================")

student = {'小智': '1002', 'info':['小张','1006','man']}
st = student.copy()
print(st)
st['小智']='1005'
print(st)
print(student)
st['info'].remove('man')
print(st)
print(student)
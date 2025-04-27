# li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
# v1 = [i for i in li if i > 66]
# v2 = [j for j in li if j < 66]
# res_dic = {"k1":v1,"k2":v2}
# print(res_dic)
#
# v1 = []
# v2 = []
# for i in li:
#     if i > 66:
#         v1.append(i)
#     if i < 66:
#         v2.append(i)
# dic_output = {'k1': v1,
#               'k2': v2}
# print(dic_output)
from sys import stderr

from 两数相加 import result
from 字典练习 import student

# friends_dic = {"zl": 23, "zff": 24, "jwj": 22}
# for k, v in friends_dic.items():
#     print(f"姓名：{k}， 年龄：{v}")
# for name, age in friends_dic.items():
#     age = age +1
#     friends_dic[name] = age
# print(friends_dic)

students = [
    {"name": "张三", "age": 23, "score": 88, "tel": "23423532", "gender": "男"},
    {"name": "李四", "age": 26, "score": 80, "tel": "12533453", "gender": "女"},
    {"name": "王五", "age": 15, "score": 58, "tel": "56453453", "gender": "男"},
    {"name": "赵六", "age": 16, "score": 57, "tel": "86786785", "gender": "不明"},
    {"name": "小明", "age": 18, "score": 98, "tel": "23434656", "gender": "女"},
    {"name": "小红", "age": 23, "score": 72, "tel": "67867868", "gender": "女"},
]

# 不及格学生的名字和成绩以及人数
num = 0
for i in students:
    if i["score"] < 60:
        num += 1
        print(i["name"], i["score"])
print(num)

# 未成年人数
teem_num = 0
for i in students:
    if i["age"] < 18:
        teem_num += 1
print(teem_num)

# 手机尾号是8的学生的名字
for i in students:
    if int(i["tel"][-1]) == 8:
        print(i["name"])

# 打印最高分和对应的学生的名字
max_score = 0
max_student = None
for i in students:
    if i["score"] > max_score:
        max_score = i["score"]
        max_student = i["name"]
print(max_student, max_score)

# 将列表按学生成绩从大到小排序
score = [i["score"] for i in students]
out_put = sorted(score)
print(out_put)
# 名字也打印出来
sorted_students = sorted(students, key=lambda x:x['score'])
for i in sorted_students:
    print(i['name'], i['score'])





'''
for循环: 重复做“已知次数”的事情
while循环: 重复做“未知次数”的事情
'''
# # for
# for i in range(5):
#     print(i)

# # while
# password = "123456"
# while True:
#     pwd = input("请输入密码：")
#     if pwd == password:
#         print("密码正确，欢迎登录")
#         break
#     else:
#         print("密码错误，请重试")

'''
break: 跳出循环
continue: 跳过当前循环，继续下一次循环
'''
for i in range(1, 100):
    if i % 3 == 0:
        print("找到第一个被3整除的数字：", i)
        break

for i in range(1, 11):
    if i % 2 == 0:
        continue  # 跳过偶数
    print(i)
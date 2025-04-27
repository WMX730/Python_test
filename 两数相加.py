'''
给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
例如： 输入：l1 = [2,4,3], l2 = [5,6,4] 输出：[7,0,8]
'''

l1 = [2,4,3]
l2 = [5,6,4]

a = ''
for i in l1:
    a += str(i)
a = int(a)

b = ''
for i in l2:
    b += str(i)
b = int(b)

c = a + b
result = []
for l in str(c):
    result.append(int(l))
output = result[::-1]
print(output)


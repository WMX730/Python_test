'''
给你一个整数x，如果x是一个回文整数，返回true;否则，返回 false。
回文数:是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如: 121 是回文，而 123 不是。
'''

print("请输入数值")
x = input()
str_x = str(x)
new_str = str_x[::-1]
if new_str == str_x:
    print("Ture")
else:
    print("False")


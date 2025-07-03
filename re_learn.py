'''
第三方库 re 的用法：处理正则表达式
在字符串中执行模式匹配、搜索、替换和分割等操作
'''

import re
text  = ["car_abc123","bike_456", "car_xyz789"]  # 定义一个字符串列表
pattern = r"car_\w*\d+"  # 匹配以"car_"开头，后面跟着任意字母和数字的字符串
for i in text:
        match = re.search(pattern, i)  # 在text中搜索符合pattern的字符串
        if match:
            print("匹配成功:", match.group())  # 输出匹配到的字符串
'''
给你一个字符串s请你反转字符串中单词的顺序。单词是由非空格字符组成的字符串。s中使用至少一个空格将字符串中的单词分隔开
例如： 输入：s = "the sky is blue"  输出："blue is sky the"
'''

s = "the sky is blue"
s = "a good   example"
list_s = []
for i in s.split():
    list_s.append(i)
result = list_s[::-1]
str_s = ''
for j in result[:]:
    str_s += j + ' '
print(str_s)
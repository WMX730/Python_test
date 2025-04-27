'''
给定一个字符串s，请你找出其中不含有重复字符的最长子串的长度。
例如：  输入: s = "abcabcbb"  输出: 3
'''

s = "pwwkew"
max_length = 0
for i in range(len(s)):
    current_length = 0
    a = []
    for j in range(i, len(s)):
        if s[j] in a:
            break
        a.append(s[j])
        current_length += 1
    max_length = max(max_length, current_length)
print(max_length)

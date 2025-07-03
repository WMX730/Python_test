'''
字符串的用法split(),分割后成为list
'''

# 默认按空格分隔
text = "hello world openai"
parts = text.split()
print(parts)  

# 指定分割符号
data = "name,age,gender"
fields = data.split(",")
fields = data.split(",")[0] # 取特定的值name
print(fields) 

# 限制分割次数
s = "a-b-c-d"
print(s.split("-", 1))  # ['a', 'b-c-d']
print(s.split("-", 2))  # ['a', 'b', 'c-d']

# 练习
str = "2024-07-03 15:00:01"
data = str.split()[0]
time = str.split()[1]
print(data) 
print(time)  

str = "clip1234_location_beijing_type_car.json"
clip_id = str.split("_")[0]
location = str.split("_")[2]
type = str.split("_")[-1].split(".")[0]  # 去掉后缀.json
file_type = str.split("_")[-1].split(".")[1]  # 去掉后缀.json
print(clip_id)
print(location)
print(file_type)

str = "key1=value1;key2=value2;key3=value3" 
result = {}
pairs = str.split(";")
for pair in pairs:
    if "=" in pair:
        key,value = pair.split("=", 1)  
        result[key] = value
print(result)  



'''
两种写入csv的方法
'''

# 方法一：使用pandas库
import pandas as pd

# 单列
num = [1,2,3,4,5,6,7,8,9,10]
df = pd.DataFrame({"num": num})
df.to_csv("num.csv", index=False, header=False)  # index=False表示不写入行索引，header=False表示不写入列名
# 多列
name = ["Alice", "Bob", "Charlie"]
id = [1,2,3]
df = pd.DataFrame({"name": name, "id": id})
df.to_csv("name_id.csv", index=False)  # index=False表示不写入行索引，header=False表示不写入列名


# 方法二：使用csv库
import csv

# 单列
num = [1,2,3,4,5,6,7,8,9,10]
with open("num.csv",mode="w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["num"])  # 写表头
    for n in num:
        writer.writerow([n])
# 多列
name = ["Alice", "Bob", "Charlie"]
id = [1,2,3]
with open("name_id.csv",mode="w",newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["name", "id"])  # 写表头
    for n, i in zip(name, id):
        writer.writerow([n, i])


'''
两种读取csv的方法
'''

# 方法一：使用pandas库
import pandas as pd

df = pd.read_csv("num.csv") 

# 方法二：使用csv库
import csv

with open("num.csv",mode="r") as file:
    reader = csv.reader(file)


'''
读取远程文件  使用refile库
'''

import refile

with refile.smart_open(csv, 'r') as f:
    df = pd.read_csv(f)

'''
df = pd.read_csv("num.csv")
df的一些功能
'''
for index, row in df.iterrows():
    print(index, row["name"])
    # index是行索引，row是每一行的数据
df.head()  # 查看前5行数据
df.tail()  # 查看后5行数据
df.info()  # 查看数据类型和缺失值情况
df['col_name'] # 选取某一列
df[['col1', 'col2']] # 选取多列
df.loc[3]   # 根据标签选取第3行数据
df.iloc[3]  # 根据位置选取第3行数据
df[df['name'] > 3]  # 条件筛选
df['new_col'] = df['col1'] + 1 # 新增列
df.loc[0,'name'] = 'Tom'       # 修改某个值
df.drop(columns=['col1'])      # 删除某一列
df.drop(index=[0, 1])          # 删除某几行数据
df.sort_values(by='col1', ascending=False) # 排序
df.drop_duplicates(subset='name') # 删除重复值
df['name'].mean()      # 计算均值
df['name'].sum()       # 计算和
df['name'].max()       # 计算最大值
df['name'].value_counts() # 计算频数
df.groupby('name')     # 分组统计
df.fillna(0)           # 填充缺失值
df.dropna()            # 删除缺失值

'''
fileIdList[fileListTotal.index(bosPath)]
找出bosPath在fileListTotal中的索引位置
然后根据索引位置找到fileIdList中的对应值
'''


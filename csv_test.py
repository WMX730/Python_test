import pandas as pd

df = pd.read_csv("test.csv")
# print(df.head()) 
# df.info() 
# print(df.loc[3])  
# print(df.iloc[3])

# 获取某一个分组的所有数据
# woman_data = df[df['gender'] == 'woman']
# grouped = df.groupby('gender') 
# print(grouped.groups) # 查看分组情况
# woman_group = grouped.get_group('woman')

# 筛选信息
filtered = df[df['age'] == 25][['id','gender']]
print(df.columns)
print(filtered)



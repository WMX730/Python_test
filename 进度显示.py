from tqdm import tqdm
import time

# 基础用法
for i in tqdm(range(10)):
    time.sleep(2)

# 普通用法
def task(x):
    time.sleep(1)
    return x * x

# 方法一
results = []
for i in tqdm(range(10)):
    results.append(task(i))

# 方法二
results = [task(i) for i in tqdm(range(10))]
for x in tqdm(range(10)):
    result = task(x)
    results.append(result)

# 方法三
task_list = [1, 2, 3, 4, 5]
for item in tqdm(task_list):
    result = task(item)

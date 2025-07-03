# from multiprocessing import Pool
# import time

# def worker(name):
#     for i in range(5):
#         print(f"{name} 正在运行 第{i}次")
#         time.sleep(10)

# if __name__ == '__main__':
#     names = [f"进程{i}" for i in range(10)]

#     with Pool(processes=5) as pool:
#         pool.map(worker, names)

''''
带进度条
'''
from tqdm.contrib.concurrent import process_map
import time

def task(x):
    time.sleep(5)
    return x * x

if __name__ == '__main__':
    process_map(task, range(10), max_workers=4)

''''
process_map(func, iterable, max_workers=None, chunksize=1)
    func: 需要执行的函数
    iterable: 需要迭代的对象
    max_workers: 进程池的大小，默认为CPU核数  （默认：max_workers=None ）
    chunksize: 每个进程处理的任务数量，默认为 1
'''

import multiprocessing
print(multiprocessing.cpu_count())  # 获取 CPU 核数

def process_singel_task(task):
    print(f"正在处理任务 {task}")
num_workers = multiprocessing.cpu_count()
with multiprocessing.Pool(processes=num_workers) as pool:
    pool.map(process_singel_task, tasks)


'''
多进程统计
   在多进程中,每个子进程都是独立内存空间,不能直接享有变量
   让每个进程返回一个状态,主进程汇总
'''


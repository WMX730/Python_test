'''
线程池
'''

from concurrent.futures import ThreadPoolExecutor
import time 

def worker(name):
    for i in range(5):
        print(f" {name} 正在运行  第{i}次")
        time.sleep(10)

names = [f"线程{i}" for i in range(10)]

with ThreadPoolExecutor(max_workers=5) as pool:
    pool.map(worker, names)


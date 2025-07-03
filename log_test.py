import os
import argparse
import logging

# 获取当前脚本所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 配置日志
logging.basicConfig(
    level=logging.INFO,  # 设置日志级别为 INFO
    format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
    handlers=[
        # logging.StreamHandler(),  # 输出到控制台
        logging.FileHandler(os.path.join(current_dir, "test.log"), mode="w")  # 输出到文件 test.log
    ]
)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--a", type=int)
    parser.add_argument("--b", type=int)

    args = parser.parse_args()
    a = args.a
    b = args.b

    result = a + b
    print("task1 finished")
    print("a+b=", result)

    if result % 2 == 1:
        result -= 1
        print("task2 finished")
        print("result is:", result)
    else:
        result /= 2
        print("task3 finished")
        print("result is:", result)
        print("已写入日志")
        logging.info(f"result is:{result}")

if __name__ == "__main__":
    main()

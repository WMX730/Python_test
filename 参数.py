import argparse

parser = argparse.ArgumentParser(description="关于参数解析器的描述")

parser.add_argument("--a", type=str, default=0, help="解释")
parser.add_argument("--b", type=str, default=0, help="解释")

args = parser.parse_args()

'''
参数：
    位置参数：不带--, 调用时必须传入
    可选参数：带--,调用时可以不传入
parse.add_argument(name, type, defult, help)  
'''
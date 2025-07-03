import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--a", type=str, default=0, help="参数a的解释")
parser.add_argument("--b", type=str, default=0, help="参数b的解释")
args = parser.parse_args()

a = args.a
b = args.b

print(f"参数a的值: {a}")
print(f"参数b的值: {b}")
print("Finish!")
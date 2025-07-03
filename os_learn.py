import os

os.getcwd()  # 获取当前工作目录
os.mkdir('test_dir')  # 创建目录
os.makedirs('test_dir/sub_dir')  # 创建多层目录
os.listdir('test_dir')  # 列出目录下的文件和子目录

# 路径操作 os.path
os.path.join('abc','bcd')   # 拼接路径
os.path.exists('test_dir')  # 判断路径是否存在
os.path.isfile('test_dir')  # 判断是否是文件
os.path.isdir('test_dir')  # 判断是否是目录
os.path.split('test_dir/sub_dir/file_z10.txt')  # 分离路径和文件名
print(os.path.split('test_dir/sub_dir/file_z10.txt'))  # ('test_dir/sub_dir', 'file.txt')        

# 获取z10
path = 'test_dir/sub_dir/file_z10.txt'
file_name = os.path.split(path)[1]  # 获取文件名
name_without_ext = os.path.splitext(file_name)[0]  # 去掉扩展名
print(name_without_ext)  # file_z10

# 更改文件后缀
print(os.path.splitext('file_z10.txt')[0]+'.md')

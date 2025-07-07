import json
'''
open(file,mode,encoding='utf-8',errors=None) as f:
    json.dump = (obj,f,indent,ensure_ascii,sort_keys,separators)

说明:   file:文件路径/文件名
        mode:文件打开模式：'r'读(默认),'w'写入,'a'追加,'rb'二进制读取
        encoding:文件编码格式(默认utf-8)
        errors:错误处理方式(默认None)

        obj:要写入python的数据
        f:写入目标文件对象(就是f)
        indent:缩进级别(默认None,不缩进)(一般选2/4)
        ensure_ascii:是否转义中文,False(保留中文)
        sort_keys:是否对字典的key进行排序(默认False)
        separators:分隔符(默认(',',':'))
'''

import json

data = {"name": "张三", "age": 20}

# 写入JSON文件
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

# 读取JSON文件
with open("user.json","r",encoding="utf-8") as f:
    data = json.load(f)

info = {
    '小明': {
        'fruits': ['苹果', '草莓', '香蕉'],
        'money': 89
    },
    '小刚': {
        'fruits': ['葡萄', '橘子', '樱桃'],
        'money': 87
    }
}

f = []
m = 0
for i in info.values():
    f += i['fruits']
    m += i["money"]
print(f)
print(m)


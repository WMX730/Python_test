'''
给你两个正整数x和y，分别表示价值为75和10的硬币的数目。
Alice和 Bob正在玩一个游戏。每一轮中，Alice先进行操作，Bob后操作。
每次操作中，玩家需要拿出价值 总和为115的硬币。如果一名玩家无法执行此操作，那么这名玩家输掉游戏。
两名玩家都采取 最优策略，请你返回游戏的赢家。
例如： 输入：x = 2, y = 7  输出："Alice"
'''

players = ["Alice", "Bob"]
coin1 = 75
coin2 = 10
x = 0
y = 4
a = y // 4
if x > a:
    if a % 2 == 0:
        print("赢家为：", players[1])
    else:
        print("赢家为：", players[0])
else:
    if x % 2 == 0:
        print("赢家为：", players[1])
    else:
        print("赢家为：", players[0])


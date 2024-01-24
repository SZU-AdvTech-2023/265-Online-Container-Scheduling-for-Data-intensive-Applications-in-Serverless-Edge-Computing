import heapq

import numpy as np
import dijkstra as dijk
import sys

"""

input: container information:Ain(αin)(二维矩阵）, Bin（βin）(二维矩阵）, Win1n1（三维矩阵）, Ci(一维数组）
       network condition: Cn(一维数组）, Yn（γn） (一维数组）, p(常量）.
output:Xin, Yin, Fin1n2, Zn
decision parameter: I, Ndatai, Linkn, Hin, AAin(α'in), Din(δin), Ln, Zn
"""


# 测试1
# scaleI = 1 + 2  # 0 useless
# scaleN = 1 + 3  # 0 is useless , 1 represent cloud , other represent edge servers
#
# Ain = np.zeros((scaleI, scaleN))
# a = [[0, 0, 0, 0], [1, 1, 1, 0], [1, 1, 0, 1]]  # i数据在哪个节点上  0表示在  第0个结点没用
# Bin = np.array(a)
# a.clear()
# a = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # 第i行表示第几个i 每一行表示一个图 第0行没用，第0个结点没用
#      [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 3], [0, 1, 3, 0]],
#      [[0, 0, 0, 0], [0, 0, 10, 3], [0, 10, 0, 3], [0, 3, 3, 0]]]
# Win1n2 = np.array(a)
# a.clear()
# Ci = np.array([0,0.2,0.3])
# Cn = np.array([0,6,10,8])
# Yn = np.array([0,2,4,7])
# p = 0.3




# 测试2
scaleI = 1 + 9  # 0 useless
scaleN = 1 + 3  # 0 is useless , 1 represent cloud , other represent edge servers

Ain = np.zeros((scaleI, scaleN))
a = [[0, 0, 0, 0], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0], [1, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 1]]  # i数据在哪个节点上  0表示在
Bin = np.array(a)
a.clear()
a = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],  # 第i行表示第几个i 每一行表示一个图 第0行没用，第0个结点没用
     [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 3], [0, 1, 3, 0]],
     [[0, 0, 0, 0], [0, 0, 10, 3], [0, 10, 0, 3], [0, 3, 3, 0]],
     [[0, 0, 0, 0], [0, 0, 1, 4], [0, 1, 0, 2], [0, 4, 2, 0]],
     [[0, 0, 0, 0], [0, 0, 2, 3], [0, 2, 0, 3], [0, 3, 3, 0]],
     [[0, 0, 0, 0], [0, 0, 2, 3], [0, 2, 0, 4], [0, 3, 4, 0]],
     [[0, 0, 0, 0], [0, 0, 4, 2], [0, 4, 0, 1], [0, 2, 1, 0]],
     [[0, 0, 0, 0], [0, 0, 2, 0], [0, 2, 0, 1], [0, 0, 1, 0]],
     [[0, 0, 0, 0], [0, 0, 3, 1], [0, 3, 0, 2], [0, 1, 2, 0]],
     [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 3], [0, 1, 3, 0]]]
Win1n2 = np.array(a)
a.clear()
Ci = np.array([0, 1.3, 0.5, 1.1, 0.7, 1.4, 0.4, 1.0, 2.2, 0.9])
Cn = np.array([0,1,10,8])
Yn = np.array([0,2,4,3])
p = 0.5

Xin = np.zeros((scaleI, scaleN))
Yin = np.zeros((scaleI, scaleN))
Fin1n2 = np.zeros((scaleI, scaleN, scaleN))
Zn = np.zeros(scaleN)

Linkn = np.ones((scaleI, scaleN,scaleN))
Hin = np.zeros((scaleI, scaleN))
AAin = np.zeros((scaleI, scaleN))
Din = np.zeros((scaleI, scaleN))
Ln = np.zeros(scaleN)

# N = scaleN - 1


for i in range(1, scaleI):
    """
    Gi has been constructed once Win1n2 has input
    all nodes with Bin == 0 belong to set Ndatai
    """

    a.clear()
    for j in range(1, scaleN):
        if Bin[i][j] == 0:
            a.append(j)
    Ndatai = np.array(a)
    """
    Conduct the single-sourced shortest path algorithm for node
    of Ndatai and get the shortest path and corresponding length
    Linkn to each node n in Gi.
    """
    dijk.makeAdjList(i, Win1n2)
    for Nk in Ndatai:
        Linkn[i][Nk] = dijk.dij(Nk,scaleN)
        # print(i)
        # print(Linkn[i][Nk])

    # 对于每一个结点N 找到最近的拥有i的数据的节点的距离
    for index in range(1, scaleN):
        # 找出在i中，结点n与存放i数据结点 之间最近的距离
        target = sys.maxsize
        for k in Ndatai:
            if Linkn[i][k][index] < target:
                target = Linkn[i][k][index]

        Hin[i][index] = target
        # print(Hin[i][index])
        AAin[i][index] = Ain[i][index] + Hin[i][index]
        # print(AAin[i][index])
        # print('----')

    #Suppose the increment to the objective function of P2 by
    #placing container i on node n is δin.

    for index in range(1, scaleN):
        if index == 1:
            Din[i][1] = AAin[i][1] + Ci[i] * p
        elif Zn[index] == 0:
            Din[i][index] = AAin[i][index] + Yn[index]
        else:
            Din[i][index] = AAin[i][index]

    #sort Din[i]
    sortList = []
    for index in range(1, scaleN):
        heapq.heappush(sortList,(Din[i][index], index))

    for index in range(1, scaleN):
        node = heapq.heappop(sortList)
        first = node[0]
        second = node[1]
        if Ln[second] + Ci[i] <= Cn[second]:
            Xin[i][second] = 1
            Ln[second] = Ln[second] + Ci[i]
            #找Nk
            target = 0
            for k in Ndatai:
                if Hin[i][index] == Linkn[i][k][index]:
                    target = k
                    # print(target)
                    break
            Yin[i][target] = 1
            if Zn[index] == 0:
                Zn[index] = 1
            Fin1n2[i][target][index] = 1
            break
"""
在下面打印看看结果

"""
for i in range(1, scaleI):
    print('container', i, ':')
    print('在哪个结点执行：',Xin[i])
    print('在哪个结点取数：',Yin[i])


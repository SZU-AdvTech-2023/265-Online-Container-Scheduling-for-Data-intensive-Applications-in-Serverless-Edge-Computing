import sys
import heapq

"""
    input:i, Win1n2
    output: a
"""

N = 200
h = [-1] * N
e = [0] * N
ne = [0] * N
w = [0] * N
idx = 0
# dist = [sys.maxsize] * 4
# st = [0] * 4  # 4是结点数


def add(a, b, c):
    # print(a,b,c)
    global idx
    # print(idx)
    w[idx] = c
    e[idx] = b
    ne[idx] = h[a]
    h[a] = idx
    idx = idx + 1

    return


def makeAdjList(i, Win1n2):
    # w[i][j][k]
    # print(Win1n2)
    #
    # print("------------")
    global idx
    idx = 0
    global h
    # 每一次重新建立邻接表，都要把h数组初始化
    for index in range(N):
        h[index] = -1
        e[index] = 0
        ne[index] = 0
        w[index] = 0

    arr = Win1n2[i:i + 1]
    # print(arr)
    # print("............")

    for index in range(len(arr)):
        for j in range(len(arr[index])):
            for k in range(len(arr[index][j])):
                # print(arr[index][j][k])
                if (arr[index][j][k] != 0):
                    add(j, k, arr[index][j][k])
    return


"""
    input: Nk, adjacency list
    output: Lnkn, 
"""


#Nk 是有数据的结点 num是结点个数 第0个结点不用管
def dij(Nk, num):
    # 将距离全部变为最大
    dist = [sys.maxsize] * num
    st = [0] * num # 4是结点数
    # for index in range(4):
    #     dist[index] = sys.maxsize
    #     st[index] = 0
    #
    dist[Nk] = 0
    min_heap = []
    heapq.heappush(min_heap, (0, Nk))
    while len(min_heap):
        k = heapq.heappop(min_heap)
        ver = k[1]
        distance = k[0]

        if st[ver] == 1:
            continue
        st[ver] = 1

        i = h[ver]
        while i != -1:

            j = e[i]
            if dist[j] > distance + w[i]:
                dist[j] = distance + w[i]
                heapq.heappush(min_heap, (dist[j], j))
            i = ne[i]

    return dist

import sys
# 运行超时 啊啊啊啊 啊
# 
# 
# 
if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())
    m = int(inp.readline().strip())
    root = int(inp.readline().strip())
    points = set([i for i in range(1,n+1)])
    # tree = {}
    # for i in range(1,n+1):
    #     tree[i] = {}
    tree = [[0]*(n+1) for i in range(n+1)]


    for i in range(m):
        v,u,t = list(map(int,inp.readline().strip().split()))
        tree[v][u] = t
        tree[u][v] = t
    
    # 贪心找最小结构PRIM算法
    inTree = {root:None}
    points -= {root}
    maxT = 0
    while len(inTree)<n:
        minT = []
        for src in inTree.keys():
            if minT and minT[2] == 1:
                break
            for dst in points:
                if tree[src][dst] and (not minT or tree[src][dst]<minT[2]):
                    minT = [src,dst,tree[src][dst]]
                    if minT[2] == 1:
                        break
        maxT = max(maxT, minT[2])
        tree[minT[0]][minT[1]], tree[minT[1]][minT[0]] = 0, 0
        inTree[minT[1]] = None
        if sum(tree[minT[0]]) == 0:
            points -= {minT[0]}
        points -= {minT[1]}
    print(maxT)
    


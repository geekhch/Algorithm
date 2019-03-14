import sys

if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())
    
    H,W = [],[]
    for i in range(n):
        H.append(list(map(int,inp.readline().strip().split())))
    for i in range(n):
        W.append(list(map(int,inp.readline().strip().split())))

    chat = 0
    for h in range(n):
        for w in range(n):
            #无交叉
            if H[h][1] <= W[w][0] or H[h][0] >= W[w][1]:
                continue
            else:
                cur = H[h] + W[w]
                cur.sort()
                chat += cur[2]-cur[1]
    print(chat)

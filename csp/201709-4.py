import sys

if __name__ == "__main__":
    inp = sys.stdin
    N,M = list(map(int, inp.readline().strip().split()))
    to_nodes = [[] for i in range(N+1)]
    message1 = [{i} for i in range(N+1)]
    message2 = [{i} for i in range(N+1)]
    for haha in range(M):
        s,d = list(map(int, inp.readline().strip().split()))
        to_nodes[s].append(d)

    for time in range(N-1):
        for i in range(1,N+1):
            for to in to_nodes[i]:
                message1[to].update(message1[i])
                message2[i].update(message2[to])
    count = 0
    for i in range(1,N+1):
        if len(message1[i]|message2[i]) == N:
            count+=1
    print(count)

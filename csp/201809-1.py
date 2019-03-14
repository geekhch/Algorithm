import sys

if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())
    prices = list(map(int, inp.readline().strip().split()))

    new = []
    for i in range(n):
        if i==0:
            new.append(sum(prices[:2])//2)
        elif i==n-1:
            new.append(sum(prices[i-1:])//2)
        else:
            new.append(sum(prices[i-1:i+2])//3)
    for p in new:
        print(p, end=' ')

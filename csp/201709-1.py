import sys

if __name__ == "__main__":
    inp = sys.stdin
    mon = int(inp.readline().strip())

    buy = mon//10
    give = (buy//5)*2 + (buy%5)//3
    print(buy+give)

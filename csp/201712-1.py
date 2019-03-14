import sys

if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())
    nums = list(map(int,inp.readline().strip().split()))

    ret = abs(nums[0]-nums[1])
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            ret = min(ret,abs(nums[i]-nums[j]))
    print(ret)

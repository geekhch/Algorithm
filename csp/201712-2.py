import sys

if __name__ == "__main__":
    inp = sys.stdin
    n,k = list(map(int,inp.readline().strip().split()))
    nums = [i for i in range(1,n+1)]

    count = 1
    pointer = 0
    while len(nums)>1:
        if count%10==k or count%k==0:
            nums.remove(nums[pointer])
            pointer %= len(nums)
        else:
            pointer = (pointer+1)%len(nums)
        count += 1
    print(nums[0])

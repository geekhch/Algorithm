import sys

n = 0
one = []
two = []
guess = []
def check():
    
    for i in range(n):
        if i == 0:
            guess[i]==((one[i]+one[i+1])//2)
        elif i == n:
            guess[i]==((one[i]+one[i-1])//2)
        else:
            guess[i]==(sum(one[i-1:i+2])//3)
    if guess==two:
        return True
    return False

if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())
    two = list(map(int, inp.readline().strip().split()))
    one = [1]*n
    guess = [0]*n
    i = n-1
    while True:
        one[i] += 1
        if check():
            ret = [str(e) for e in one]
            print(' '.join(ret))
            break
        elif one[i] == 20:
            for j in range(i,-1,-1):
                if one[j] == 20:
                    one[j-1] += 1
                    one[j] = 1
                else:
                    break
##            print(one)

import sys

# 全局变量
r,y,g = 0,0,0
staus = [1,3,2] # 红。绿。黄
setTime = {}

def signal(color, time, after):
    if color==0:
        return time
    color_index = staus.index(color)
    after %= (r+y+g)
    #计算到达时的状态
    while True:
        if after < time:
            time -= after
            break
        else:
            after -= time
            color_index = (color_index+1)%3 # 颜色状态转化
            color = staus[color_index]
            time = setTime[color]
    # 计算当前状态还需要等待的时间
    if color==1:
        return time
    if color==3:
        return 0
    if color == 2:
        return time+r
            
              
        


if __name__ == "__main__":
    inp = sys.stdin
    r,y,g = list(map(int,inp.readline().strip().split()))
    setTime = {1:r,3:g,2:y}
    n = int(inp.readline().strip())
    ret = 0
    for i in range(n):
        color, time = list(map(int,inp.readline().strip().split()))
        ret += signal(color,time,ret)
    print(ret)
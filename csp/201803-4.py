import sys

def Count(who,mp):
    count = mp[0].count(0)+mp[1].count(0)+mp[2].count(0)
    if who==1:
        return count+1
    if who==2:
        return -count-1

def Win(mp):
    for i in [1,2]:
        if (mp[0][0] & mp[1][1] & mp[2][2])==i or (mp[2][0] & mp[1][1] & mp[0][2])==i:
            return i
        for loc in range(3):
            if (mp[loc][0]==i)&(mp[loc][1]==i)&(mp[loc][2]==i):
                return i
            elif (mp[0][loc]==i)&(mp[1][loc]==i)&(mp[2][loc]==i):
                return i
    return 0

def dfs(curmp, who):
    i,j=0,0
    if curmp[0].count(0)+curmp[1].count(0)+curmp[2].count(0) == 0:
        return 0
    Min,Max = 10,-10
    for i in range(3):
        for j in range(3):
            if curmp[i][j] == 0:
                curmp[i][j] = who
                win = Win(curmp)

                if who==1 and win==1:
                    Max = max(Max,curmp[0].count(0)+curmp[1].count(0)+curmp[2].count(0)+1)
                    
                elif who==2 and win==2:
                    Min = min(Min,-(curmp[0].count(0)+curmp[1].count(0)+curmp[2].count(0)+1))
                    
                else:
                    if who == 1:
                        Max = max(dfs(curmp,3-who),Max)
                    else:
                        Min = min(dfs(curmp,3-who),Min)
                curmp[i][j] = 0
    if who==1:
        return Max
    return Min
    
    
if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())
    for game in range(n):
        mp = []
        for i in range(3):
            mp.append(list(map(int,inp.readline().strip().split())))
        
        who = Win(mp)
        if who:
            win = Count(who,mp)
            print(win)
            continue
        elif mp[0].count(0)+mp[1].count(0)+mp[2].count(0) == 0 or mp[0].count(0)+mp[1].count(0)+mp[2].count(0)>8:
            print(0)
            continue
        else:
            if mp[0].count(1)+mp[1].count(1)+mp[2].count(1)>mp[0].count(2)+mp[1].count(2)+mp[2].count(2):
                print(dfs(mp,2))
            else:
                print(dfs(mp,1))
        
            
            

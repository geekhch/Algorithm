import sys,json

def Search(ob, key):
    if not key[0] in ob:
        return False
    if len(key)==1:
        return ob[key[0]]
    else:
        return Search(ob[key[0]], key[1:])

if __name__ == "__main__":
    inp = sys.stdin
    n,m = list(map(int,inp.readline().strip().split()))
    ss = json.loads(''.join([inp.readline().strip() for i in range(n)]))
    search = [inp.readline().strip() for i in range(m)]
    for s in search:
        ret = Search(ss,s.split('.'))
        if ret==False:
            print('NOTEXIST')
        elif isinstance(ret, dict):
                print('OBJECT')
        else:
            print('STRING',ret)
        

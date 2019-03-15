import sys
from functools import cmp_to_key

class OP:
    def __init__(self,num,time,lend):
        self.num = num
        self.time = time
        self.lend = lend

def cmpare(op1, op2):
    if op1.time<op2.time:
        return -1
    elif op1.time>op2.time:
        return 1
    else:
        if op1.lend and not op2.lend:
            return 1
        if not op1.lend and op2.lend:
            return -1
        else:
            if op1.num<op2.num:
                return -1
            if op2.num<op1.num:
                return 1


if __name__ == "__main__":
    inp = sys.stdin
    N,K = list(map(int,inp.readline().strip().split()))
    boxes = [i for i in range(1,N+1)]
    ops = []
    for yy in range(K):
        w,s,c = list(map(int,inp.readline().strip().split()))
        op1 = OP(w,s,True)
        op2 = OP(w,s+c,False)
        ops.append(op1)
        ops.append(op2)
    #排序
    ops = sorted(ops,key=cmp_to_key(cmpare))
    
    for op in ops:
        if op.lend:
            boxes[boxes.index(op.num)] = 0
        else:
            boxes[boxes.index(0)] = op.num
    boxes = list(map(str,boxes))
    print(' '.join(boxes))

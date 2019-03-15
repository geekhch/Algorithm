import sys
from functools import cmp_to_key

nodes = []

class Node:
    def __init__(self, num):
        self.next = {}
        self.cur = []
        self.num = num
        self.Min = float('inf')

def compare(p1,p2):
    if p1[0]<p2[0]:
        return -1
    if p1[0]>p2[0]:
        return 1
    if p1[0]==p2[0]:
        if p1[1]>p2[1]:
            return -1
        if p1[1]==p2[1]:
            return 0
        return 1

if __name__ == "__main__":
    inp = sys.stdin

    n,m = list(map(int,inp.readline().strip().split()))
    nodes = [None] + [Node(i) for i in range(1,n+1)]
    nodes[1].cur.append([0,0])

    for i in range(m):
        path = list(map(int,inp.readline().strip().split()))
        nodes[path[1]].next[path[2]] = [path[0], path[3]]

    
    least = [1]
    nodes.remove
    for i in range(n+1):
        if i==0:
            node = nodes[1]
        else:
            node = None
            for node_t in nodes[1:]:
                if not node_t.num in least and (not node or (node_t.cur and node_t.Min<node.Min)):
                    node = node_t
            least.append(node.num)
            
        if node.num == n:
            print(node.Min)
            break
        # 对cur_path进行排序并删除冗余道路
        node.cur = sorted(node.cur,key=cmp_to_key(compare))
        point = 1
        while point<len(node.cur):
            if node.cur[point]>=node.cur[point-1]:
                node.cur.pop(point)
            else:
                point += 1
        
        for path in node.cur:
            for nxt_num in node.next.keys():
                if nxt_num in least:
                    continue 
                edge = node.next[nxt_num]
                if edge[0] == 0:
                    new_path = [path[0]+edge[1], 0]
                else:
                    bad_len = path[1]+edge[1]
                    new_path = [path[0]-pow(path[1],2)+pow(bad_len,2), bad_len]
                # 插入当前方案
                nxt_node = nodes[nxt_num]
                nxt_node.cur.append(new_path)
                nxt_node.Min = min(nxt_node.Min, new_path[0])
                

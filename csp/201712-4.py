import sys

nodes = []

class Node:
    def __init__(self, num):
        self.next = {}
        self.cur = []
        self.num = num
        

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
                if not node_t.num in least and (not node or (node_t.cur and node_t.cur[-1][0]<node_t.cur[-1][0])):
                    node = node_t
            least.append(node.num)

        print(node.num)
        if node.num == n:
            print(node.cur[-1][0])
            break
        
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
                # 考虑是否插入当前方案
                nxt_node = nodes[nxt_num]
                if not len(nxt_node.cur):
                    nxt_node.cur.append(new_path)
                else:
                    pot = 0
                    roads = nxt_node.cur
                    if new_path[0]< roads[-1][0] and new_path[1]>roads[-1][1]:
                        roads.append(new_path)
                    else:
                        while pot<len(roads):
                            
                            if new_path[0]>=roads[pot][0] and new_path[1]>=roads[pot][1]:
                                break
                            if new_path[0]>roads[pot][0] and new_path[1]<roads[pot][1]:
                                roads.insert(pot,new_path)
                                break
                            if new_path[0]<=roads[pot][0] and new_path[1]> roads[pot][1]:
                                pot += 1
                            if new_path[0]<=roads[pot][0] and new_path[1]<=roads[pot][1]:
                                if pot == len(roads)-1:
                                    roads[pot] = new_path
                                    break
                                else:
                                    roads.pop(pot)
                    

                        
        
    

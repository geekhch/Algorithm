import sys
##子元素和后代元素概念混淆，读题失误
nodes = []
id_index = {}
label_index = {}


class NODE:
    label = ''
    ids = ''
    number = 0
    prio = 0
    parent = None

    def __init__(self,line,number):
        self.prio = line.count('..')
        strs = line.replace('..','').split()
        if len(strs) > 1:
            self.ids = strs[1]
        self.label = strs[0].lower()
        self.number = number
        self.children = []

def singleFind(sl):
    sl = sl[0]    
    ret = [0]
    if sl[0] == '#':
        if sl in id_index:
            print(1,id_index[sl].number)
        else:
            print(0)
    else:
        if sl in label_index:
            ret[0] = len(label_index[sl])
            for n in label_index[sl]:
                ret.append(n.number)
            ret = [str(e) for e in ret]
            print(' '.join(ret))
        else:
            print(0)

def mutiHelper(nodes, sl):
    if sl[0] == '#':
        for n in nodes:
            if sl==n.ids:
                return [n]
        return []
    else:
        ret = []
        for n in nodes:
            if sl==n.label:
                ret.append(n)
        return ret

def mutiFind(nodes, sl):
    if len(sl)==1:
        ret = mutiHelper(nodes, sl[0])
        top = []
        for n in ret:
            top.append(n.number)
        top = [str(e) for e in sorted(top)]
        top.insert(0,str(len(ret)))
        print(' '.join(top))
    else:
        cur_nodes = mutiHelper(nodes, sl[0])
        children = []
        for n in cur_nodes:
            children += n.children
        return mutiFind(children, sl[1:])
        


if __name__ == "__main__":
    inp = sys.stdin
    n,m = list(map(int, inp.readline().strip().split()))

    root_str = inp.readline().strip()
    root = NODE(root_str,1)

    nodes.append([root])

    #构建文档
    for i in range(n-1):
        node = NODE(inp.readline().strip(),i+2)
        prio = node.prio
        
        if len(nodes) < prio+1:
            nodes.append([node])
        else:
            nodes[prio].append(node)
        nodes[prio-1][-1].children.append(node)
        node.parent = nodes[prio-1][-1]
        # label 索引
        if not node.label in label_index:
            label_index[node.label] = [node]
        else:
            label_index[node.label].append(node)
        # id 索引
        if node.ids:
            id_index[node.ids] = node
    # 查询文档
    for i in range(m):
        sl_raw = inp.readline().strip()
        sl = []
        for e in sl_raw.split():
            if e[0] == '#':
                sl.append(e)
            else:
                sl.append(e.lower())
        
        if len(sl)==1:
            singleFind(sl)
        else:
            deep = len(sl)
            cur = []
            ready = []
            if sl[0][0] == '#':
                if sl[0] in id_index:
                    ready = [id_index[sl[0]]]
            elif sl[0] in label_index:
                ready = label_index[sl[0]]
                
            for n in ready:
                if n.prio < len(nodes)+1-deep:
                    cur.append(n)
            mutiFind(cur, sl)
                    
            
            

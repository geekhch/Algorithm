import sys

class IP:
    pre = ''
    suf = 0
    next = None
    last = None
    def __init__(self, pre, suf):
        self.pre = pre
        self.suf = suf

def standarlize(ip):
    ip = ip.split('/')
    preffix = ip[0]
    preffix = preffix.split('.')
    ret_pre = ''
    for o in preffix:
        b = str(bin(int(o))).replace('0b','')
        b = '0'*(8-len(b)) + b
        ret_pre += b
    ret_pre = ret_pre + '0'*(32-len(ret_pre))

    if len(ip)==2:
        suffix = int(ip[1])
    else:
        suffix = len(preffix)*8
    return ret_pre, suffix

def compare(ip1,ip2):
    if ip1.pre<ip2.pre:
        return -1
    if ip1.pre==ip2.pre and ip1.suf<ip2.suf:
        return -1
    if ip1.pre==ip2.pre and ip1.suf==ip2.suf:
        return 0
    else:
        return 1

def toPrint(ip):
    pre = ip.pre
    ss = [
        str(eval('0b'+pre[:8])),
        str(eval('0b'+pre[8:16])),
        str(eval('0b'+pre[16:24])),
        str(eval('0b'+pre[24:32]))
    ]
    return '.'.join(ss) + '/' + str(ip.suf) 


if __name__ == "__main__":
    inp = sys.stdin
    n = int(inp.readline().strip())

    
    head = None
    tail = None
    for i in range(n):
        ip = inp.readline().strip()
        pre, suf = standarlize(ip)
        ip = IP(pre, suf)

        # 添加到有序队列(排序)
        if not head:
            head = ip
            tail = ip
        else:
            if compare(ip,head)<=0:
                ip.next = head
                head.last = ip
                head = ip
                continue
            node = head.next
            while node:
                if compare(ip,node) <= 0:
                    ip.last = node.last
                    ip.next = node
                    ip.last.next = ip
                    ip.next.last = ip
                    break
                node = node.next
            if not node:
                ip.last = tail
                tail.next = ip
                tail = ip

    # 扫描合并
    node = head
    while node.next:
        nxt = node.next
        if node.suf<= nxt.suf and node.pre[:node.suf] == nxt.pre[:node.suf]:
            node.next = nxt.next
            nxt.next.last = node
            del nxt
        else:
            node = nxt
    tail = node

    node = head
    while node and node.next:
        nxt = node.next
        if nxt.suf == node.suf and node.pre[nxt.suf-1] != nxt.pre[nxt.suf-1] and node.pre[:nxt.suf-1] == nxt.pre[:nxt.suf-1]:
            new = IP(node.pre[:node.suf-1] + '0'*(33-node.suf), node.suf-1)
            new.last = node.last
            new.next = nxt.next
            if node.last:
                node.last.next = new
            else:
                head = new
            if nxt.next:
                nxt.next.last = new
            else:
                tail = new
            del node,nxt
            node = new.last
        else:
            node = node.next
            
    # 遍历输出
    # 遍历输出
    node = head
    while node:
        print(toPrint(node))
        node = node.next

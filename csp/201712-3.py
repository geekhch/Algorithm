import sys
import calendar as cal
import datetime

Mon = {'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
Week = {'Sun':0, 'Mon':1, 'Tue':2, 'Wed':3, 'Thu':4, 'Fri':5, 'Sat':6}

class Work:
    def __init__(self, line):
                
        line = line.split()
        self.name = line[-1]
        self.month = [e.split('-') for e in line[3].split(',')]
        for e in self.month:
            for i in range(len(e)):
                if e[i].capitalize() in Mon:
                    e[i] = Mon[e[i].capitalize()]
        self.day = [e.split('-') for e in line[2].split(',')]
        self.hour = [e.split('-') for e in line[1].split(',')]
        self.minute = [e.split('-') for e in line[0].split(',')]
        self.weekday = [e.split('-') for e in line[4].split(',')]
        for e in self.weekday:
            for i in range(len(e)):
                if e[i].capitalize() in Week:
                    e[i] = Week[e[i].capitalize()]
                    
    def matchHelper(self, node, timecat):
        for e in node:
            if e[0]=='*' or (len(e)==1 and int(e[0])==int(timecat)) or (len(e)==2 and int(e[0])<=int(timecat) and int(e[1])>=int(timecat)):
                return True
        return False

    def match(self,time):

        if not self.matchHelper(self.minute, time[10:]):
            return False

        if not self.matchHelper(self.hour,time[8:10]):
            return False
        
        if not self.matchHelper(self.day, time[6:8]):
            return False
        
        if not self.matchHelper(self.month, time[4:6]):
            return False
                
        wee = (cal.weekday(int(time[:4]),int(time[4:6]),int(time[6:8]))+1)%7
        if not self.matchHelper(self.weekday, wee):
            return False
        return True

   
if __name__ == "__main__":
    inp = sys.stdin
    n,s,t = list(inp.readline().strip().split())
    n = int(n)
    nodes = [None]*n
    for i in range(n):
        nodes[i] = Work(inp.readline().strip())
    time = s
    t_ob = datetime.datetime(int(time[:4]),int(time[4:6]), int(time[6:8]),int(time[8:10]),int(time[10:]))
    delta = datetime.timedelta(minutes=1)
    while time!=t:
        for node in nodes:
            if node.match(time):
                print(time, node.name)
        t_ob += delta
        time = t_ob.strftime('%Y%m%d%H%M')
    

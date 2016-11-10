f = open("file11.txt",'r')
all = f.read()
all = all.split('>')[1:]

all = [w for seg in all for w in seg.split('\n',1)]
all = [seg.replace('\n','') for seg in all if all.index(seg)%2==1]

def simlr(a,b):
    c = 0
    for i in range(0,len(min(a,b))):
        if(a[i] == b[i]):
            c+=1
    return c/(len(max(a,b)))

for i in range(0,len(all)):
    a = []
    for j in range(0,len(all)):
        a.append((1-simlr(all[i],all[j])).__round__(6))
    print(*a)


from collections import defaultdict

f=  open("file17.txt",'r')
s = f.read()
s = s.split('>')[1:]
s = [seg.split('\n',1)[1].replace('\n','') for seg in s]

f = open("blosum.txt",'r')
dict1,blosum = {},{}
line = f.readline().replace('\n','').replace(' ','')
[dict1.update({i:j}) for i,j in enumerate(list(line))]

k=0
for line in f.readlines():
    line = line[2:].replace('\n','')
    w = line.split(' ')
    w = [int(i) for i in w if(i!= '')]
    [blosum.update({(dict1[k],dict1[i]):j}) for i,j in enumerate(w)]
    k=k+1

def gl_align_aff_pen(s, t):
    T,Td,Tr = defaultdict(int),defaultdict(int),defaultdict(int)
    open_pen = -11
    ext_pen = -1
    A={}

    for i in range(0,len(s)):
        T[-1,i] = open_pen+i*ext_pen
        Td[-1,i] = open_pen
        Tr[-1,i] = open_pen+i*ext_pen
        A[-1,i] = (-1,i-1)

    for i in range(0, len(t)):
        T[i, -1] = open_pen+i*ext_pen
        Td[i,-1] = open_pen+i*ext_pen
        Tr[i,-1] = open_pen
        A[i,-1] = (i-1,-1)

    for i,si in enumerate(list(s)):
        for j,ti in enumerate(list(t)):
            Td[j,i] = max(Td[j-1,i] + ext_pen,
                          T[j-1,i] + open_pen)
            Tr[j,i] = max(Tr[j,i-1] + ext_pen,
                          T[j,i-1] + open_pen)
            T[j,i],A[j,i] = max((T[j-1,i-1] + blosum[si,ti], (j-1,i-1)),
                         (Td[j, i], (j-1, i)),
                         (Tr[j, i], (j, i-1)))
    return T[len(t)-1,len(s)-1],A

def aff_pen_traceback(A,s,t):
    j,i = max(list(A.keys()))
    ns1, ns0 = [], []
    while (j != -1 or i != -1):
        if (A[j, i][0] < j):
            ns1.append(t[j])
        else:
            ns1.append('-')
        if (A[j, i][1] < i):
            ns0.append(s[i])
        else:
            ns0.append('-')
        j, i = A[j, i]
    ns1 = ''.join(reversed(ns1))
    ns0 = ''.join(reversed(ns0))
    return ns1,ns0

val,A = gl_align_aff_pen(s[0],s[1])
s1,s2 = aff_pen_traceback(A,s[0],s[1])

print(val,s2,s1,sep='\n')

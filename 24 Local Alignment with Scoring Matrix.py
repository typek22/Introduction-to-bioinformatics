from collections import defaultdict

f=  open("file16.txt",'r')
s = f.read()
s = s.split('>')[1:]
s = [seg.split('\n',1)[1].replace('\n','') for seg in s]

f = open("pam250.txt",'r')
dict1,pam = {},{}
line = f.readline().replace('\n','').replace(' ','')
[dict1.update({i:j}) for i,j in enumerate(list(line))]

k=0
for line in f.readlines():
    line = line[2:].replace('\n','')
    w = line.split(' ')
    w = [int(i) for i in w if(i!= '')]
    [pam.update({(dict1[k],dict1[i]):j}) for i,j in enumerate(w)]
    k=k+1

def score(a,b):
    if(a== '-' or b == '-'):
        return(-5)
    else:
        return(pam[a,b])

def loc_align(s, t):
    T = defaultdict(int)
    A={}
    for i in range(0,len(s)):
        T[-1,i] = T[-1,i-1] + score('-',s[i])
        A[-1,i] = (-1,i-1)

    for i in range(0, len(t)):
        T[i, -1] = T[i-1, -1] + score('-', t[i])
        A[i,-1] = (i-1,-1)

    for i,si in enumerate(list(s)):
        for j,ti in enumerate(list(t)):
            T[j,i],A[j,i] = max((T[j-1,i-1] + score(si,ti), (j-1,i-1)),
                         (T[j, i - 1] + score('-', si), (j, i - 1)),
                         (T[j - 1, i] + score(ti, '-'), (j - 1, i)),
                         (0, (0,0)))
    return T,A

def loc_align_traceback(T,A):
    val,pos = max([(j, i) for i, j in enumerate(T.values())])
    j,i = list(T.keys())[pos]

    ns0,ns1 = [],[]
    while (T[j,i] != 0):
        if (A[j, i][0] < j):
            ns1.append(s[1][j])
        if (A[j, i][1] < i):
            ns0.append(s[0][i])
        j, i = A[j, i]

    ns1 = ''.join(reversed(ns1))
    ns0 = ''.join(reversed(ns0))
    return(ns0,ns1,val)


tab,A = loc_align(s[0],s[1])
(s1,s2,val) = loc_align_traceback(tab,A)

print(val,s1,s2,sep='\n')

from collections import defaultdict

f=  open("file14.txt",'r')
s = f.read()
s = s.split('>')[1:]
s = [seg.split('\n',1)[1].replace('\n','') for seg in s]

def score(a,b):
    if(a == '-' or b == '-'):
        return(-2)
    if(a==b):
        return(2)
    else:
        return(-1)

T = defaultdict(int)
A={}
for i in range(0,len(s[0])):
    T[-1,i] = T[-1,i-1] + score('-',s[0][i])
    A[-1,i] = (-1,i-1)

for i in range(0, len(s[1])):
    T[i, -1] = T[i-1, -1] + score('-', s[1][i])
    A[i,-1] = (i,-1)

for i,s0i in enumerate(list(s[0])):
    for j,s1j in enumerate(list(s[1])):
        T[j,i],A[j,i] = max((T[j-1,i-1] + score(s0i,s1j), (j-1,i-1)),
                     (T[j, i - 1] + score('-', s0i), (j, i - 1)),
                     (T[j - 1, i] + score(s1j, '-'), (j - 1, i)))


j,i = len(s[1])-1,len(s[0])-1
ns1,ns0 = [],[]
while (j!=-1 or i!=-1):
    if(A[j,i][0] < j):
        ns1.append(s[1][j])
    else:
        ns1.append('-')
    if (A[j, i][1] < i):
        ns0.append(s[0][i])
    else:
        ns0.append('-')
    j,i = A[j,i]

ns1 = ''.join(reversed(ns1))
ns0 = ''.join(reversed(ns0))
print(sum([1 for a,b in zip(ns0,ns1) if a != b]),ns0,ns1,sep='\n')

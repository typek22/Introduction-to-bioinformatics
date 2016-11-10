from collections import defaultdict

f=  open("file15.txt",'r')
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

def score(a,b):
    if(a== '-' or b == '-'):
        return(-5)
    else:
        return(blosum[a,b])

T = defaultdict(int)
A={}
for i in range(0,len(s[0])):
    T[-1,i] = T[-1,i-1] + score('-',s[0][i])
    A[-1,i] = (-1,i-1)

for i in range(0, len(s[1])):
    T[i, -1] = T[i-1, -1] + score('-', s[1][i])
    A[i,-1] = (i-1,-1)

for i,s0i in enumerate(list(s[0])):
    for j,s1j in enumerate(list(s[1])):
        T[j,i],A[j,i] = max((T[j-1,i-1] + score(s0i,s1j), (j-1,i-1)),
                     (T[j, i - 1] + score('-', s0i), (j, i - 1)),
                     (T[j - 1, i] + score(s1j, '-'), (j - 1, i)))

print(T[len(s[1])-1,len(s[0])-1])
from collections import defaultdict

f=  open("file13.txt",'r')
s = f.read()
s = s.split('>')[1:]
s = [seg.split('\n',1)[1].replace('\n','') for seg in s]

def score(a,b):
    if(a==b):
        return(0)
    else:
        return(1)

T = defaultdict(int)
for i in range(0,len(s[0])):
    T[-1,i] = T[-1,i-1] + score('-',s[0][i])

for i in range(0, len(s[1])):
    T[i, -1] = T[i-1, -1] + score('-', s[1][i])

for i,s0i in enumerate(list(s[0])):
    for j,s1j in enumerate(list(s[1])):
        T[j,i] = min(T[j-1,i-1] + score(s0i,s1j),
                     T[j, i - 1] + score('-', s0i),
                     T[j - 1, i] + score(s1j, '-'))

print(T[len(s[1])-1,len(s[0])-1])

f  = open('file7.txt','r')
input = f.read()
str = input.split('\n',1)
str = str[1].replace('\n','')

P = []
P.append(0)
Q = 0;
for i in range(1,len(str)):
    strtmp = str[0:(i+1)]
    Q = 0
    for j in range(P[i-1]+1,0,-1):
        a = strtmp[0:j]
        b = strtmp[(i-j+1):(i+1)]
        if(strtmp[0:j] == strtmp[(i-j+1):(i+1)]):
            P.append(j)
            Q = 1;
            break
    if(Q == 0):
        P.append(0)

print(*P)




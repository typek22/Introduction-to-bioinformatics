from collections import Counter
from itertools import product

f  = open('file5.txt','r')
input = f.read()
str = input.split('\n',1)[1].replace('\n','')

all = [''.join(s) for s in product('ACTG',repeat = 4)]
dict = {key:0 for key in all}

a = [str[i:i+4] for i in range(0,len(str)-4+1)]
C = Counter(a)
for key,val in C.items():
    dict[key] = val

vals=[key for val,key in sorted(dict.items())]
print(*vals)



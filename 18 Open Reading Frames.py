from Bio.Seq import Seq
import re

f = open('file10.txt','r')
str = f.read()
str = str.split('\n',1)
str[1] = str[1].replace('\n','')
seq = Seq(str[1])
rev = seq.reverse_complement()
str = seq.__str__()+"      "+rev.__str__()

l = [[0],[-3]]
for i in range(0,len(str)+1):
    a = str[(i):(i + 3)]
    if (a == 'TGA' or a == 'TAG' or a == 'TAA'):
        for j in range(i-3,-1,-3):
            if(str[j:(j+3)]=='ATG'):
                l[0].append(j)
                l[1].append(i)
            if (str[j:(j+3)] == 'TGA' or str[j:(j+3)] == 'TAG' or str[j:(j+3)] == 'TAA' or str[j:(j+3)] == "   "):
                break

g = []
for i in range(1,len(l[0])):
    g.append(Seq(str[(l[0][i]):l[1][i]]).translate())

g = list(set(g))
[print(x) for x in g]


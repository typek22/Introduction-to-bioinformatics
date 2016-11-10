from Bio.Seq import Seq
import re

f = open('file9.txt','r')
seq = Seq(f.read())
rev = seq.reverse_complement()
str = seq.__str__()+"      "+rev.__str__()

l = [[0],[-3]]
for i in range(0,len(str)+1):
    a = str[(i):(i + 3)]
    if (a == 'TGA' or a == 'TAG' or a == 'TAA' or i == (len(str)) ):
        for j in range(i-3,-1,-3):
            if(str[j:(j+3)]=='ATG'):
                l[0].append(j)
                l[1].append(i)
            if (str[j:(j+3)] == 'TGA' or str[j:(j+3)] == 'TAG' or str[j:(j+3)] == 'TAA' or str[j:(j+3)] == '   '):
                break

m = [b-a for a,b in zip(l[0],l[1])]
m.__delitem__(0)
idx = m.index(max(m))
print(Seq(str[(l[0][idx+1]):l[1][idx+1]]).translate())
from itertools import product

f  = open('file6.txt','r')
input = f.read()
str = input.split('\n',1)
num = int(str[1])
str = str[0].replace(' ','')

all = [''.join(s) for s in product(str,repeat=num)]
all = sorted(all)
print(*all,sep='\n')



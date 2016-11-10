import re

f  = open('file4.txt','r')
input = f.read()
strs = input.split('\n')

a = [m.start()+1 for m in re.finditer('(?='+strs[1]+')', strs[0])]
print(*a)


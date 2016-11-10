f=  open("file12.txt",'r')
s = f.read()
s = s.split('\n')
print(sum([1 for a,b in zip(s[0],s[1]) if a != b]))
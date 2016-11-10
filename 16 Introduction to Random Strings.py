from collections import Counter
import math

f = open("file8.txt",'r')
str = f.read()
str = str.split("\n")
probs = str[1].split(" ")

C = Counter(str[0])
out = [math.log((float(pr)/2)**(C['G']+C['C'])*((1-float(pr))/2)**(C['A']+C['T']),10) for pr in probs]
print(*out)


from collections import Counter

s = 'We tried list and we tried dicts also we tried Zen'

list = s.split(' ')
C = Counter(list)

for key, value in C.items():
    print(key,value)





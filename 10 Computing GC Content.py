f  = open('file2.txt','r')
sents = f.read().split('>')
sents.pop(0)
L = []
for sent in sents:
    idx = sent.find('\n')
    a = (sent.count('C',idx) + sent.count('G',idx))
    b = (sent.count('A',idx) + sent.count('T',idx))
    L.append(a/(a+b))
k = L.index(max(L))
print(sents[k][0:sents[k].find('\n')])
print(max(L)*100)



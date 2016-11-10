dic = {'UUU':'F'  ,    'CUU':'L'  ,    'AUU':'I'    ,  'GUU':'V',
'UUC':'F'   ,   'CUC':'L'   ,   'AUC':'I'   ,   'GUC':'V',
'UUA':'L'   ,   'CUA':'L'   ,   'AUA':'I'   ,   'GUA':'V',
'UUG':'L'   ,   'CUG':'L'   ,   'AUG':'M'   ,   'GUG':'V',
'UCU':'S'   ,   'CCU':'P'   ,   'ACU':'T'   ,   'GCU':'A',
'UCC':'S'   ,   'CCC':'P'   ,   'ACC':'T'   ,   'GCC':'A',
'UCA':'S'   ,   'CCA':'P'   ,   'ACA':'T'   ,   'GCA':'A',
'UCG':'S'   ,   'CCG':'P'   ,   'ACG':'T'   ,   'GCG':'A',
'UAU':'Y'   ,   'CAU':'H'   ,   'AAU':'N'   ,   'GAU':'D',
'UAC':'Y'   ,   'CAC':'H'   ,   'AAC':'N'   ,   'GAC':'D',
'UAA':''    ,   'CAA':'Q'   ,   'AAA':'K'   ,   'GAA':'E',
'UAG':''    ,   'CAG':'Q'   ,   'AAG':'K'   ,   'GAG':'E',
'UGU':'C'   ,   'CGU':'R'   ,   'AGU':'S'   ,   'GGU':'G',
'UGC':'C'   ,   'CGC':'R'   ,   'AGC':'S'   ,   'GGC':'G',
'UGA':''    ,   'CGA':'R'   ,   'AGA':'R'   ,   'GGA':'G',
'UGG':'W'   ,   'CGG':'R'   ,   'AGG':'R'   ,   'GGG':'G' }

f   = open('file3.txt','r')
str = f.read()
str = str.replace('\n','')

triples = [str[i:i+3] for i in range(0,(len(str)-2),3) ]

letters = [dic[x] for x in triples]
sent = ''.join(letters)
print(sent)
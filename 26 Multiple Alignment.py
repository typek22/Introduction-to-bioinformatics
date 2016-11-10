from collections import defaultdict

f=  open("file18.txt",'r')
s = f.read()
s = s.split('>')[1:]
s = [seg.split('\n',1)[1].replace('\n','') for seg in s]

def score(a,b,c,d):
    l = (a,b,c,d)
    s = 0
    for i in range(0,4):
        for j in range(i+1,4):
            if(l[i] != l[j]):
                s = s -1
    return s

T = defaultdict(int)
A={}
for w in range(0,4):
    a = [[-1, -1, -1, -1],[-1,-1,-1,-1]]
    for i in range(0,len(s[w])):
        a[0][w] = i
        a[1][w] = i-1
        T[tuple(a[0])] = T[(tuple(a[1]))] + score(s[w][i], '-', '-', '-')
        A[tuple(a[0])] = tuple(a[1])

for w in range(0,4):
    for y in range(w+1,4):
        a = [[-1, -1, -1, -1] for _ in range(0,4)]
        for i, si in enumerate(list(s[w])):
            for j, sj in enumerate(list(s[y])):
                a[0][w], a[0][y] = i, j
                a[1][w], a[1][y] = i - 1,j - 1
                a[2][w], a[2][y] = i - 1, j
                a[3][w], a[3][y] = i, j - 1
                T[tuple(a[0])], A[tuple(a[0])] = max(
                    (T[tuple(a[1])] + score('-', '-', s[w][i], s[y][j]), tuple(a[1])),
                    (T[tuple(a[2])] + score('-', '-', s[w][i], '-'), tuple(a[2])),
                    (T[tuple(a[3])] + score('-', '-', '-', s[y][j]), tuple(a[3])))

for w in range(0,4):
    y = [0, 1, 2, 3]
    y.remove(w)
    a = [[-1,-1,-1,-1] for _ in range(0,8)]
    for k, s2k in enumerate(list(s[y[2]])):
        for j, s1j in enumerate(list(s[y[1]])):
            for i, s0i in enumerate(list(s[y[0]])):
                a[0][y[0]], a[0][y[1]], a[0][y[2]] = i, j, k
                a[1][y[0]], a[1][y[1]], a[1][y[2]] = i - 1, j - 1, k - 1
                a[2][y[0]], a[2][y[1]], a[2][y[2]] = i, j - 1, k - 1
                a[3][y[0]], a[3][y[1]], a[3][y[2]] = i - 1, j, k - 1
                a[4][y[0]], a[4][y[1]], a[4][y[2]] = i - 1, j - 1, k
                a[5][y[0]], a[5][y[1]], a[5][y[2]] = i - 1, j, k
                a[6][y[0]], a[6][y[1]], a[6][y[2]] = i, j - 1, k
                a[7][y[0]], a[7][y[1]], a[7][y[2]] = i, j, k - 1

                T[tuple(a[0])], A[tuple(a[0])] = max(
                    (T[tuple(a[1])] + score('-', s0i, s1j, s2k), tuple(a[1])),
                    (T[tuple(a[2])] + score('-', '-', s1j, s2k), tuple(a[2])),
                    (T[tuple(a[3])] + score('-', s0i, '-', s2k), tuple(a[3])),
                    (T[tuple(a[4])] + score('-', s0i, s1j, '-'), tuple(a[4])),
                    (T[tuple(a[5])] + score('-', s0i, '-', '-'), tuple(a[5])),
                    (T[tuple(a[6])] + score('-', '-', s1j, '-'), tuple(a[6])),
                    (T[tuple(a[7])] + score('-', '-', '-', s2k), tuple(a[7])))

# i,j,k,l
for l,s3l in enumerate(list(s[3])):
    for k,s2k in enumerate(list(s[2])):
        for j, s1j in enumerate(list(s[1])):
            for i, s0i in enumerate(list(s[0])):
                T[i,j,k,l],A[i,j,k,l] = max((T[i - 1, j - 1, k - 1, l-1] + score(s0i, s1j, s2k, s3l), (i - 1, j - 1, k - 1, l - 1)),
                                            (T[i - 1, j - 1, k - 1, l] + score(s0i, s1j, s2k, '-'),(i - 1, j - 1, k - 1, l)),
                                            (T[i - 1, j - 1, k, l - 1] + score(s0i, s1j, '-', s3l),(i - 1, j - 1, k, l - 1)),
                                            (T[i - 1, j, k - 1, l - 1] + score(s0i, '-', s2k, s3l),(i - 1, j, k - 1, l - 1)),
                                            (T[i, j - 1, k - 1, l - 1] + score('-', s1j, s2k, s3l),(i, j - 1, k - 1, l - 1)),
                                            (T[i - 1, j - 1, k, l] + score(s0i, s1j, '-', '-'),(i - 1, j - 1, k, l)),
                                            (T[i - 1, j, k - 1, l] + score(s0i, '-', s2k, '-'),(i - 1, j, k - 1, l)),
                                            (T[i, j - 1, k - 1, l] + score('-', s1j, s2k, '-'),(i, j - 1, k - 1, l)),
                                            (T[i - 1, j, k, l - 1] + score(s0i, '-', '-', s3l),(i - 1, j, k, l - 1)),
                                            (T[i, j - 1, k, l - 1] + score('-', s1j, '-', s3l),(i, j - 1, k, l - 1)),
                                            (T[i, j, k - 1, l - 1] + score('-', '-', s2k, s3l),(i, j, k - 1, l - 1)),
                                            (T[i, j, k, l - 1] + score('-', '-', '-', s3l),(i, j, k, l - 1)),
                                            (T[i, j, k - 1, l] + score('-', '-', s2k, '-'),(i, j, k - 1, l)),
                                            (T[i, j - 1, k, l] + score('-', s1j, '-', '-'),(i, j - 1, k, l)),
                                            (T[i - 1, j, k, l] + score(s0i, '-', '-', '-'),(i - 1, j, k, l)))


i,j,k,l = len(s[0])-1,len(s[1])-1,len(s[2])-1,len(s[3])-1
ns0,ns1,ns2,ns3 = [],[],[],[]
while (i!=-1 or j!=-1 or k!= -1 or l != -1):
    if(A[i,j,k,l][0] < i):
        ns0.append(s[0][i])
    else:
        ns0.append('-')
    if (A[i,j,k,l][1] < j):
        ns1.append(s[1][j])
    else:
        ns1.append('-')
    if (A[i,j,k,l][2] < k):
        ns2.append(s[2][k])
    else:
        ns2.append('-')
    if (A[i,j,k,l][3] < l):
        ns3.append(s[3][l])
    else:
        ns3.append('-')
    i,j,k,l = A[i,j,k,l]

ns0 = ''.join(reversed(ns0))
ns1 = ''.join(reversed(ns1))
ns2 = ''.join(reversed(ns2))
ns3 = ''.join(reversed(ns3))
print(T[len(s[0])-1,len(s[1])-1,len(s[2])-1,len(s[3])-1],ns0,ns1,ns2,ns3,sep='\n')

# # i
# for i in range(0,len(s[0])):
#     T[i,-1,-1,-1] = T[i-1,-1,-1,-1] + score(s[0][i],'-','-','-')
#     A[i,-1,-1,-1] = (i-1,-1,-1,-1)
# # j
# for j in range(0, len(s[1])):
#     T[-1,j,-1,-1] = T[-1,j-1,-1, -1] + score('-', s[1][j],'-','-')
#     A[-1, j, -1, -1] = (- 1, j-1, -1, -1)
# # k
# for k in range(0, len(s[2])):
#     T[-1,-1,k,-1] = T[-1,-1,k-1, -1] + score('-','-',s[2][k],'-')
#     A[-1, -1, k, -1] = (- 1, -1, k-1, -1)
# # l
# for l in range(0, len(s[3])):
#     T[-1,-1,-1,l] = T[-1,-1,-1, l-1] + score('-','-','-',s[3][l])
#     A[-1, -1, -1, l] = (- 1, -1, -1, l-1)


# # k,l
# for l,s3l in enumerate(list(s[3])):
#     for k,s2k in enumerate(list(s[2])):
#         T[-1, -1, k, l], A[-1, -1, k, l] = max(
#             (T[- 1, - 1, k - 1, l - 1] + score('-', '-', s2k, s3l), (- 1, - 1, k - 1, l - 1)),
#             (T[- 1, - 1, k - 1, l] + score('-', '-', s2k, '-'), (- 1, - 1, k - 1, l)),
#             (T[- 1, - 1, k, l - 1] + score('-', '-', '-', s3l), (- 1, - 1, k, l - 1)))
#
# # j,l
# for l,s3l in enumerate(list(s[3])):
#     for j,s1j in enumerate(list(s[1])):
#         T[-1, j, -1, l], A[-1, j, -1, l] = max(
#             (T[- 1, j - 1, - 1, l - 1] + score('-', s1j, '-', s3l), (- 1, j - 1, - 1, l - 1)),
#             (T[- 1, j, - 1, l - 1] + score('-', '-', '-', s3l), (- 1, j, - 1, l - 1)),
#             (T[- 1, j - 1, - 1, l] + score('-', s1j, '-', '-'), (- 1, j - 1, - 1, l)))
#
# # i,l
# for l,s3l in enumerate(list(s[3])):
#     for i,s0i in enumerate(list(s[0])):
#         T[i, -1, -1, l], A[i, -1, -1, l] = max(
#             (T[i - 1, - 1, - 1, l - 1] + score(s0i, '-', '-', s3l), (i - 1, - 1, - 1, l - 1)),
#             (T[i, - 1, - 1, l - 1] + score('-', '-', '-', s3l), (i, - 1, - 1, l - 1)),
#             (T[i - 1, - 1, - 1, l] + score(s0i, '-', '-', '-'), (i - 1, - 1, - 1, l)))
#
# # j,k
# for k,s2k in enumerate(list(s[2])):
#     for j,s1j in enumerate(list(s[1])):
#         T[-1, j, k, -1], A[-1, j, k, -1] = max(
#             (T[- 1, j - 1, k - 1, - 1] + score('-', s1j, s2k, '-'), (- 1, j - 1, k - 1, - 1)),
#             (T[- 1, j, k - 1, - 1] + score('-', '-', s2k, '-'), (- 1, j, k - 1, - 1)),
#             (T[- 1, j - 1, k, -1] + score('-', s1j, '-', '-'), (- 1, j - 1, k, - 1)))
#
# # i,k
# for k,s2k in enumerate(list(s[2])):
#     for i,s0i in enumerate(list(s[0])):
#         T[i, -1, k, -1], A[i, -1, k, -1] = max(
#             (T[i - 1, - 1, k - 1, - 1] + score(s0i, '-', s2k, '-'), (i - 1, - 1, k - 1, - 1)),
#             (T[i, - 1, k - 1, - 1] + score('-', '-', s2k, '-'), (i, - 1, k - 1, - 1)),
#             (T[i - 1, - 1, k, -1] + score(s0i, '-', '-', '-'), (i - 1, - 1, k, - 1)))
#
# # i,j
# for j,s1j in enumerate(list(s[1])):
#     for i,s0i in enumerate(list(s[0])):
#         T[i, j, - 1, -1], A[i, j, - 1, -1] = max(
#             (T[i - 1, j - 1, - 1, - 1] + score(s0i, s1j, '-', '-'), (i - 1, j - 1, - 1, - 1)),
#             (T[i, j - 1, - 1, - 1] + score('-', s1j, '-', '-'), (i, j - 1, - 1, - 1)),
#             (T[i - 1, j, - 1, -1] + score(s0i, '-', '-', '-'), (i - 1, j, - 1, - 1)))

# # j,k,l
# for l,s3l in enumerate(list(s[3])):
#     for k,s2k in enumerate(list(s[2])):
#         for j, s1j in enumerate(list(s[1])):
#             T[-1, j, k, l], A[-1, j, k, l] = max(
#                 (T[- 1, j - 1, k - 1, l - 1] + score('-', s1j, s2k, s3l), (- 1, j - 1, k - 1, l - 1)),
#                 (T[- 1, j, k - 1, l - 1] + score('-', '-', s2k, s3l), (- 1, j, k - 1, l - 1)),
#                 (T[- 1, j - 1, k, l - 1] + score('-', s1j, '-', s3l), (- 1, j - 1, k, l - 1)),
#                 (T[- 1, j - 1, k - 1, l] + score('-', s1j, s2k, '-'), (- 1, j - 1, k - 1, l)),
#                 (T[- 1, j - 1, k, l] + score('-', s1j, '-', '-'), (- 1, j - 1, k, l)),
#                 (T[- 1, j, k - 1, l] + score('-', '-', s2k, '-'), (- 1, j, k - 1, l)),
#                 (T[- 1, j, k, l - 1] + score('-', '-', '-', s3l), (- 1, j, k, l - 1)))
#
#
#
# # i,k,l
# for l, s3l in enumerate(list(s[3])):
#     for k, s2k in enumerate(list(s[2])):
#         for i, s0i in enumerate(list(s[0])):
#             T[i, -1, k, l], A[i, -1, k, l] = max(
#                 (T[i - 1, - 1, k - 1, l - 1] + score(s0i, '-', s2k, s3l), (i - 1, - 1, k - 1, l - 1)),
#                 (T[i, - 1, k - 1, l - 1] + score('-', '-', s2k, s3l), (i, - 1, k - 1, l - 1)),
#                 (T[i - 1, - 1, k, l - 1] + score(s0i, '-', '-', s3l), (i - 1, - 1, k, l - 1)),
#                 (T[i - 1, - 1, k - 1, l] + score(s0i, '-', s2k, '-'), (i - 1, - 1, k - 1, l)),
#                 (T[i - 1, - 1, k, l] + score(s0i, '-', '-', '-'), (i - 1, - 1, k, l)),
#                 (T[i, - 1, k - 1, l] + score('-', '-', s2k, '-'), (i, - 1, k - 1, l)),
#                 (T[i, - 1, k, l - 1] + score('-', '-', '-', s3l), (i, - 1, k, l - 1)))
#
# # i,j,l
# for l, s3l in enumerate(list(s[3])):
#     for j, s1j in enumerate(list(s[1])):
#         for i, s0i in enumerate(list(s[0])):
#             T[i, j, -1, l], A[i, j, -1, l] = max(
#                 (T[i - 1, j - 1, - 1, l - 1] + score(s0i, s1j, '-', s3l), (i - 1, j - 1, - 1, l - 1)),
#                 (T[i, j - 1, - 1, l - 1] + score('-', s1j, '-', s3l), (i, j - 1, - 1, l - 1)),
#                 (T[i - 1, j, - 1, l - 1] + score(s0i, '-', '-', s3l), (i - 1, j, - 1, l - 1)),
#                 (T[i - 1, j - 1, - 1, l] + score(s0i, s1j, '-', '-'), (i - 1, j - 1, - 1, l)),
#                 (T[i - 1, j, - 1, l] + score(s0i, '-', '-', '-'), (i - 1, j, - 1, l)),
#                 (T[i, j - 1, - 1, l] + score('-', s1j, '-', '-'), (i, j - 1, - 1, l)),
#                 (T[i, j, - 1, l - 1] + score('-', '-', '-', s3l), (i, j, - 1, l - 1)))
#
# # i,j,k
# for k, s2k in enumerate(list(s[2])):
#     for j, s1j in enumerate(list(s[1])):
#         for i, s0i in enumerate(list(s[0])):
#             T[i, j, k, - 1], A[i, j, k, - 1] = max(
#                 (T[i - 1, j - 1, k - 1, - 1] + score(s0i, s1j, s2k, '-'), (i - 1, j - 1, k - 1, - 1)),
#                 (T[i, j - 1, k - 1, - 1] + score('-', s1j, s2k, '-'), (i, j - 1, k - 1, - 1)),
#                 (T[i - 1, j, k - 1, - 1] + score(s0i, '-', s2k, '-'), (i - 1, j, k - 1, - 1)),
#                 (T[i - 1, j - 1, k, - 1] + score(s0i, s1j, '-', '-'), (i - 1, j - 1, k, - 1)),
#                 (T[i, j, k - 1, - 1] + score('-', '-', s2k, '-'), (i, j, k - 1, - 1)),
#                 (T[i, j - 1, k, - 1] + score('-', s1j, '-', '-'), (i, j - 1, k, - 1)),
#                 (T[i - 1, j, k, - 1] + score(s0i, '-', '-', '-'), (i - 1, j, k, - 1)))

from collections import Counter

s = 'TATATGTGGAACTTCTTGGTCTCATCGTCAGCCTCACCTAGGCGCCAGATTTACATAGTAAATGCATGCAGAATAATATGCATTTTTATTCTGTGTACCCACCCGCTTGATGACGCAGTAGCTCTAATCAGCGCCAAAGGAACGATCACGGTCTCCCGGCTGAGAAATTTCTAAGCGTTTACTTTCCGTCGGATCTTCATTTTTCTGGAAAAGTAAAAGACCCGCCGGACGCGGAGAGGCACACACGGATTCTGGTTAGTTTATATTACTCGATGACGCGTATGGATCCTACGTTGGGCTAGGTTTCTGTCGAGGACAGTCCTTTTCCCCCTAGCTAAACCTGGAAGTATAAATCAAAAGAAAATGGGGTGCCATCAATCAATCGGGTCCCCATTTGACAAAAGGTTGTTTCATCGCTCTAAGGTTCTGCCGCAGTATGAAAATACAGATACTCTTGAGCTAATTTGATGTGCGAACGCAACGCCAGGTCGTCGTCTTAAGCCGGTTCGACTCGGTGGCTAGCGTGGGTCTTGGACAGTGGGCTGATAGTCCATATGGGTCCCTTGCTCGTTCGGGCCCGAGCTCAGTGGCGTCGGTTCATGAATGGTGAGGCCCGGGTCCACTGGTAGCCGTTGCAGAAGACCAACACTGATACGCAACCATGTGAATGTGGCAAAAAACCGGAACCTCAATAGTGGTCCCAAGAATCTATGGTGCAGTAAGACAACCCACAACGCATGATATACTTGTAGGGAGCCCGCTCTCGATGCCTCCCGTCCTTAGATTGATATGCGTGCGCTATATTCATTACCTTTCTTGCAAGACTCGGGTGTTTTCTTGTGTGTGTACGAATCATCGACCCTGCGTAGACCAAGATGGCACTTCCCAGAATGAAAGGCGCCTGTCATGGTCGCCCATCGGACTAGATGCTCTGGCTTTAAATTTATCCTTACAGTATACCGAATGAGGATACACTTTAGAGTAGA'
l = list(s)
C = Counter(l)

print(C['A'],C['C'],C['G'],C['T'])






import numpy as np

"""
s1:
    String A = m, String B = n
s2:

"""
# initial
# A, B string
strA = "bcdabab"
strB = "cbacbaaba"
m = len(strA)
n = len(strB)

# matrix
matrix = np.array([[0 for i in range(m + 1)] for i in range(m + 1)])
pos = m
MAX = 0

# print(matrix)

while MAX <= pos:
    posA = pos
    LCS = 1
    upperB = n + 1
    while posA >= 0 and upperB >= 0:
        if pos == m or LCS > MAX:
            matrix[LCS - 1][posA] = 0
        lowerB = max(0, matrix[LCS - 1][posA])
        posB = upperB - 1
        while posB >= lowerB and strA[posA - 1] != strB[posB - 1]:
            posB = posB - 1
        if posB >= lowerB:
            upperB = posB
        else:
            upperB = matrix[LCS - 1, posA]
        matrix[LCS - 1, posA - 1] = upperB
        if upperB == 0:
            LCS = LCS - 1
        MAX = max(MAX, LCS)
        LCS = LCS + 1
        posA = posA - 1
    pos = pos - 1

print(matrix)

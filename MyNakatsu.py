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
pos = 0
MAX = 0

while MAX <= m - pos:
    posA = pos
    LCS = 1
    lowerB = 0
    while posA < m and lowerB < n:
        upperB = n - 1
        posB = lowerB
        while posB <= upperB and strA[posA] != strB[posB]:
            posB = posB + 1
        if posB <= upperB:
            lowerB = posB
        else:
            break
        matrix[LCS - 1, posA + 1] = lowerB + 1
        if lowerB == -1:
            LCS = LCS - 1
        MAX = max(MAX, LCS)
        LCS = LCS + 1
        posA = posA + 1
    pos = pos + 1

print(matrix)

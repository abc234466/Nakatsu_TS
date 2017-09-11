


# dvalue = [[0 for i in range(len(str2))] for i in range(len(str1))]


# def dsNakatsu():
#     i = 0
#     j = 0
#     ci = i
#     cj = j
#     while ci < len(str1)  or cj < len(str2) :
#         while str1[ci] != str2[cj] and cj < len(str2) - 1:
#             cj += 1
#         if cj != len(str2) - 1 and cj > dvalue[ci - 1][cj - 1]:
#             dvalue[ci][cj] = min(cj, dvalue[ci - 1][cj])
#             ci += 1
#             cj += 1
#         else:
#             dvalue[ci][cj] = dvalue[ci - 1][cj]
#             i+=1
#             ci = i
#             cj = j
#
#
#
# dsNakatsu()


# print(dvalue)

str1 = "actgcttcg"
str2 = "tcacgtcc"


def d(i, s):
    if i < s:
        return float('inf')
    elif s == 0:
        return 0
    j = d(i - 1, s - 1)
    if j == float('inf'):
        return ('inf')
    while str1[i - 1] != str2[j] and j < len(str2):
        j += 1
        if j == len(str2):
            break
    if j < len(str2) :
        return min(j + 1, d(i - 1, s))
    else:
        return d(i - 1, s)


print(d(6, 5))

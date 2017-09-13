'''
    i must be larger than s , i.e. i >= s
    i < s  is impossible


'''

str1 = "bcdabab"
str2 = "cbacbaaba"


def d(i, s):
    if s == 0:
        return 0
    elif i < s or d(i - 1, s - 1) >=len(str2) :
        return float('inf')
    j = d(i - 1, s - 1)  # lower bound

    while str1[i - 1] != str2[j] and j < len(str2):  # find next match, i.e. str1[i] == str2[j]
        j += 1
        if j == len(str2):
            break
    if j < len(str2):
        return min(j + 1, d(i - 1, s))
    else:
        return d(i - 1, s)



for i in range(len(str1)+1):
    for j in range(len(str2)):
        print(d(i, j), end=' ')
    print()

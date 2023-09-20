# 피보나치 수 5


n = int(input())

# pibo = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
pibo = [0, 1, 1]

# f_p = 0
# s_p = 1
# t_p = 1
# i >= 2

for i in range(2, n+1):
    pibo[i] = pibo[i-1] + pibo[i-2]
    pibo.append(pibo[i])

# print(pibo)


print(pibo[n])
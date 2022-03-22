# 소수

m = int(input())
n = int(input())

# m~n 소수의 합
# 소수 체크
mn_list = list()
for k in range(m, n+1):
    if k == 1:
        pass
    elif k == 2:
        mn_list.append(k)
    for i in range(2, k):
        if k % i == 0:
            break
        else i == k - 1:
            mn_list.append(i)

if len()

print(sum(mn_list))
print(min(mn_list))
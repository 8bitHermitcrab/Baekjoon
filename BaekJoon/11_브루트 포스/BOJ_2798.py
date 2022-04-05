# 블랙잭

n, m = map(int, input().split())

num = list(map(int, input().split()))
len_num = len(num)
result = 0

for i in range(len_num -2):
    for j in range(i+1, len_num -1):
        for k in range(j+1, len_num):
            if(num[i] + num[j] + num[k] > m):
                continue
            else:
                result = max(result, num[i] + num[j] + num[k])

print(result)


# https://velog.io/@jeongdopark/Algorithm-python-%EB%B0%B1%EC%A4%80-2798%EB%B2%88
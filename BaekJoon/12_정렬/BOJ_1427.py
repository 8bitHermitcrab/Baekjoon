# 소트인사이드

n = int(input())

for i in str(n):
    n_list = list(map(int, str(n)))

# 내림차순
n_list.sort(reverse=True)

for i in n_list:
    print(i, end='')
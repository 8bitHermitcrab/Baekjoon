import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

cnt = [0] * N

for i in range(N):
   
    if i == 0:
        cnt[0] = 1
        continue
    
    # maxinfo = [index, count]
    maxinfo = [-1, -1]
    for j in range(i):
        if num[i] > num[j]:
            if cnt[j] > maxinfo[1]:
                maxinfo = [j, cnt[j]]

    if maxinfo != [-1, -1] :
        cnt[i] = cnt[maxinfo[0]] + 1
    else:
        cnt[i] = 1


print(max(cnt))
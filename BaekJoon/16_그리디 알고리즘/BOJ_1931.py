# 회의실 배정

n = int(input())

time = [[0]*2 for _ in range(n)]
# [[0, 0], [0, 0], [0, 0]]

for i in range(n):
    start, end = map(int, input().split())
    time[i][0] = start
    time[i][1] = end
    # print(time)


time.sort(key = lambda x: (x[1], x[0]))

count = 1
end_time = time[0][1]
# print(end_time)

for i in range(1, n):
    if time[i][0] >= end_time:
        count += 1
        end_time = time[i][1]

print(count)

# https://suri78.tistory.com/26
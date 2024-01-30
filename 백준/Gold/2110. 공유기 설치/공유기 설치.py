import sys
input = sys.stdin.readline

n, c = map(int, input().split())

arr = []

for _ in range(n):
    arr.append(int(input()))
arr.sort()

start = 1
end = arr[-1] - arr[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    curr = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= curr + mid:
            cnt += 1
            curr = arr[i]

    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
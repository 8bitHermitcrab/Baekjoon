# 좋은 친구

# n줄의 학생, k등수 차이
n, k = map(int, input().split())
students = [0] * n
data = [0] * 21
count = 0

for rank in range(n):
    # 이름의 길이
    name = len(input().strip())
    # rank 인덱스에 name 값
    students[rank] = name
    if rank > k:
        data[students[rank - k - 1]] -= 1
        count += data[1]
        data[1] += 1
print(count)
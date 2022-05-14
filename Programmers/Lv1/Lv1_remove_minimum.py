# 제일 작은 수 제거하기

# arr = [4, 3, 2, 1]
arr = [10]

answer = []

if arr == [10]:
    answer = [-1]
else:
    mini = min(arr)
    arr.remove(mini)
    answer = arr
print(answer)
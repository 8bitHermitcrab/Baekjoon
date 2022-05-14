# 행렬의 덧셈

arr1 = [
    [1,2],
    [2,3]
    ]
# [0][0], [0][1]
arr2 = [
    [3,4],
    [5,6]
    ]

arr3 = [
    [1],
    [2]
    ]
# [0], [1]

# print(len(arr3[0]))


# 행 길이
row = len(arr1[0])
# 열 길이
col = len(arr1)

answer = []
# print(row)
# print(col)

for i in range(col):
    temp = []
    for j in range(row):
        temp.append(arr1[i][j] + arr2[i][j])
    print(temp)
    answer.append(temp)
    
print(answer)


# https://velog.io/@cosmos/Programmers%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%96%89%EB%A0%AC%EC%9D%98-%EB%8D%A7%EC%85%88-python
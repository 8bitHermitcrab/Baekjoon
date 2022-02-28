# OX퀴즈

t = int(input())

for i in range(t):
    quiz = input()
    score = 0
    count = 0
    for j in list(quiz):
        if j == 'O':
            count += 1
            score += count
        if j == 'X':
            count = 0
    print(score)

'''
quiz = [input() for _ in range(t)]

results = []
O_list = []
X_list = []

# print(quiz)

for i in range(80):
    # O의 개수 세기
    count_O = count(quiz[i] == 'O')
    # O 점수 합 구하기
    sum_O = count_O / 2
    # O 점수 합 리스트에 넣기
    O_list.append(sum_O)

    # X의 개수 세기
    count_X = quiz[i].count('X')
    # X 점수 합 구하기
    sum_X = count_X / 2
    # X 점수 합 리스트에 넣기
    X_list.append(sum_X)

    # O 점수에서 X 점수 빼기
    results.append(O_list[i] - X_list[i])

for i in range(t):
    print(results[i])

https://velog.io/@jsw8050/%EB%B0%B1%EC%A4%80-1%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-8958%EB%B2%88-OX-%ED%80%B4%EC%A6%88-Python
'''
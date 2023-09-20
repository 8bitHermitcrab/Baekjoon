# 쉽게 푸는 문제

a, b = map(int, input().split())

n_list = [0]

# i 값을 i번 n_list에 넣기
for i in range(1000):
    for j in range(i):
        n_list.append(i)

# n_list를 a부터 b까지 잘라서 모두 더하기
print(sum(n_list[a:b+1]))

'''
for i in range(b+1):
    # result = (a * a) + (...) + (b * b)
    n_i = (a + i) * (a + i)
    # n_list.append(n_i)
    n_i += n_i

print(n_i)

https://velog.io/@woga1999/BOJ-1292%EB%B2%88-%EC%89%BD%EA%B2%8C-%ED%91%B8%EB%8A%94-%EB%AC%B8%EC%A0%9C-Python
'''
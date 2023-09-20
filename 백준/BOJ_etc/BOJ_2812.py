# 크게 만들기

N, K = map(int, input().split())

num = list(input())

stack = []
k = K

for i in range(N):
    while k > 0 and stack and stack[-1] < num[i]:
        print(f'i, N, K = {i, N, K}')
        print(f'num = {num}')
        print(f'stack = {stack}')
        print(f'k = {k}')
        stack.pop()
        k -= 1
        print(f'stack = {stack}')
        print(f'k = {k}')
    stack.append(num[i])

print(''.join(stack[:N-K]))

# https://jokerldg.github.io/algorithm/2021/05/25/make-big.html



n, k = map(int, input().split())



# 0 만들기

import copy

t = int(input())

def solution():
    global n, answer
    n = int(input())
    answer = []
    op(2, '1')
    print()

def op(now, ans):
    global answer
    if now == n+1:
        calc(ans)
        return

    op(now+1, ans+ ' '+str(now))
    op(now+1, ans+ '+'+str(now))
    op(now+1, ans+ '-'+str(now))


def calc(ans):
    temp = ans.replace(' ', '')
    if eval(temp) == 0:
        print(ans)

for _ in range(t):
    solution()


# https://westmino.tistory.com/47
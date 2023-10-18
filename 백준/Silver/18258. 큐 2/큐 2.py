import sys
from collections import deque

n = int(input())

quene = deque([])

for i in range(n):
    sent = sys.stdin.readline().split()

    if sent[0] == 'push':
        quene.append(sent[1])
    elif sent[0] == 'front':
        if len(quene) == 0:
            print(-1)
        else:
            print(quene[0])
    elif sent[0] == 'back':
        if len(quene) == 0:
            print(-1)
        else:
            print(quene[-1])
    elif sent[0] == 'size':
        print(len(quene))
    elif sent[0] == 'empty':
        if len(quene) == 0:
            print(1)
        else:
            print(0)
    elif sent[0] == 'pop':
        if len(quene) == 0:
            print(-1)
        else:
            print(quene.popleft())
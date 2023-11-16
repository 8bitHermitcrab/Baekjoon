import sys
input = sys.stdin.readline
n = int(input())

office = dict()

for _ in range(n):
    name, act = map(str, input().split())

    if act == 'enter':
        office[name] = act
    else:
        del office[name]

office = sorted(office.keys(), reverse=True)

for i in office:
    print(i)
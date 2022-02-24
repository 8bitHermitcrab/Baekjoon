# 더하기 사이클

ab = int(input())
count = 1
check = ab

def Numbers(ab):
    # 10의 자리
    a = ab // 10
    # 1의 자리
    b = ab % 10
    # 26 : 2+6 = 8
    c = (a + b) % 10
    d = (b * 10) + c
    return d

while ab!= Numbers(check):
    count += 1
    check = Numbers(check)

print(count)



""" while True:
    count += 1
    # 10의 자리
    a = ab // 10
    # 1의 자리
    b = ab % 10
    # 26 : 2+6 = 8
    c = (a + b) % 10
    d = b*10 + c

    check = d """
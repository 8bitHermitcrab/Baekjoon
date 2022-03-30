# 직각삼각형

while True:
    a = list(map(int, input().split()))
    max_num = max(a)
    if sum(a) == 0:
        break
    a.remove(max_num)

    if a[0] **2 + a[1] **2 == max_num **2:
        print('right')
    else:
        print('wrong')

'''
while True:
    a, b, c = map(int, input().split())

    if (a**2) + (b**2) == 0:
        break
    
    if (a**2) + (b**2) == (c**2):
        print('right')
    else:
        print('wrong')

'''


# https://pacific-ocean.tistory.com/132
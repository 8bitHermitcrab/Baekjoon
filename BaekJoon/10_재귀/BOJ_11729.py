# 하노이 탑 이동 순서

# 이동경로를 담을 list
move = []

def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n-1, a, c, b)
        move.append([a, c])
        hanoi(n-1, b, a, c)


hanoi(int(input()), 1, 2, 3)

# print(f'move = {move}')

for row in move:
    # print(f'row = {row}')
    for i in row:
        r = ' '.join(str(i))
        # print(f'r = {r}')
        result = '\n'.join(r)

print(len(move))
print(result)
#print('\n'.join([' '.join(str(i) for i in row) for row in move]))


'''
n = int(input())

a = []
temp = []
b = []
k = 0
k_ab = dict()

move1_2 = '1 2'
move2_3 = '2 3'
move1_3 = '1 3'

# 4321
# 432 1 
# 43  1  2
# 43    21
# 4  3  21
# 4 312 
#   312 4
#   12  43
# 1 2 43
# 1   432
#      4321
# a temp b
for i in range(1, n+1):
    # a탑 만들기
    a.append(i)
    if n == 1:
        k = 1
        print(k)
        print(move1_3)
    else:
        k += 1
        temp.append(i)
        b.append(i+)
        k_ab[k] = 
'''



# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9Chanoi-top-in-python
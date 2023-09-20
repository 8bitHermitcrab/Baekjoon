# 음계

x = list(map(int, input().split()))

# c:1, d:2, e:3, f:4, g:5, a:6, b:7, C:8
a = [i for i in range(1, 9)]
print(f'a = {a}')
b = [j for j in range(8, 0, -1)]
print(f'b = {b}')

if x == a:
    print('ascending')
elif x == b:
    print('descending')
else:
    print('mixed')

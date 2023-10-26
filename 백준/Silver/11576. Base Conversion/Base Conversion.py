a, b = map(int, input().split())
m = int(input())
m_list = list(map(int, input().split()))
m_list.reverse()

num10 = 0
for i in range(m):
    num10 += m_list[i] * (a ** i)

result = []
while num10 // b:
    result.append(num10 % b)
    num10 = num10 // b
result.append(num10)

result.reverse()
print(' '.join(map(str, result)))
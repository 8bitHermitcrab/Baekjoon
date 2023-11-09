n = int(input())
channel = [input() for _ in range(n)]

idx, idx2 = channel.index('KBS1'), channel.index('KBS2')

if idx > idx2:
    idx2 += 1

print(('1' * idx) + ('4' * idx) + ('1' * idx2) + ('4' * (idx2 - 1)))
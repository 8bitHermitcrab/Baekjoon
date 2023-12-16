n, g = input().split()

member = set()
for i in range(int(n)):
    member.add(input().rstrip())

game = len(member)

if g == 'Y':
    print(game)
elif g == 'F':
    print(game // 2)
else:
    print(game // 3)
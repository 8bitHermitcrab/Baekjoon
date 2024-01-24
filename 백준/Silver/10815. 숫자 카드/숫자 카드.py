import sys
input = sys.stdin.readline

n = int(input())
card_list = list(map(int, input().split()))
m = int(input())
check_list = list(map(int, input().split()))

card_dict = dict()
for i in range(len(card_list)):
    card_dict[card_list[i]] = 0

for j in range(m):
    if check_list[j] not in card_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')
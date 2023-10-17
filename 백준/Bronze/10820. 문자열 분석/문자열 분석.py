import sys

while True:
    sent = sys.stdin.readline().rstrip('\n')

    if not sent:
        break

    cnt_list = [0] * 4

    for i in sent:
        if i.islower() == True:
            cnt_list[0] += 1
        elif i.isupper() == True:
            cnt_list[1] += 1
        elif i.isdigit() == True:
            cnt_list[2] += 1
        elif i.isspace() == True:
            cnt_list[3] += 1

    print(*cnt_list)
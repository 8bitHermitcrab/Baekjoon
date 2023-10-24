n, b = map(int, input().split())

temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def base_num(num, base):
    a, x = divmod(num, base)

    if a == 0:
        return temp[x]
    else:
        return base_num(a, base) + temp[x]

print(base_num(n, b))
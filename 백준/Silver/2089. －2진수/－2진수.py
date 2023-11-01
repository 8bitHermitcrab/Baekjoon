def base_2(n, result):
    if n == 0:
        result.append(0)
        return
    if n == 1:
        result.append(1)
        return
    if n % 2 == 0:
        result.append(0)
        base_2(n // -2, result)
    elif n < 0:
        result.append(1)
        base_2((n // -2) + 1, result)
    else:
        result.append(1)
        base_2((n // -2) + 1, result)

n = int(input())
result = []
base_2(n, result)
result.reverse()
print(''.join(str(i) for i in result))
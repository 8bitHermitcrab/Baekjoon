n, m = map(int, input().split())

def cnt_num(n, k):
    cnt = 0
    while n:
        n //= k
        cnt += n
    return cnt

cnt5 = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num((n - m), 5)
cnt2 = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num((n - m), 2)

result = min(cnt5, cnt2)
print(result)
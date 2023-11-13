n, k = map(int, input().split())

n_list = list(map(int, input().split()))
n_list = sorted(n_list)

print(n_list[k-1])
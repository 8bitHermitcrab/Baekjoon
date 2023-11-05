import math

h, w, n, m = map(int, input().split())

i = math.ceil(h / (n + 1))
j = math.ceil(w / (m + 1))

result = i * j
print(result)
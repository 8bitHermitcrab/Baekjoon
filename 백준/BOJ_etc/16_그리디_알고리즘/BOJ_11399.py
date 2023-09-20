# ATM

n = int(input())
time = list(map(int, input().split()))

result = 0

time.sort()

for i in range(n):
    for j in range(i+1):
        print(f'time[{j}] = {time[j]}')
        print(f'result = {result}')
        result += time[j]
print(result)

# https://pacific-ocean.tistory.com/227

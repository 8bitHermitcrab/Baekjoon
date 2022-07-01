# 베르랑 공준

def getPrim(n):
    nums = [True] * (n)
    for i in range (2, int(n**0.5) + 1):
        if nums[i] == True:
            for j in range(i+i, n, i):
                nums[j] = False
    return [i for i in range(2, n) if nums[i] == True]

while True:
    n = int(input())

    if n == 0:
        break
    prime_list = getPrim(2*n + 1)
    answer_list = [num for num in prime_list if num > n]
    print(len(answer_list))



#https://somjang.tistory.com/entry/BaekJoon-4948%EB%B2%88-%EB%B2%A0%EB%A5%B4%ED%8A%B8%EB%9E%91-%EA%B3%B5%EC%A4%80-Python
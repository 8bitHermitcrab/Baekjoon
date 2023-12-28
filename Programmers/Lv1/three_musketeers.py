# 삼총사
def solution(number):
    comb_list = []

    def ncr(n, answer, r):
        if n == len(number):
            if len(answer) == r:
                temp = [i for i in answer]
                print(f'temp = {temp}')
                comb_list.append(temp)
                print(f'comb_list = {comb_list}')
            return
        answer.append(number[n])
        print(f'answer = {answer}')
        ncr(n+1, answer, r)
        answer.pop()
        print(f'answer = {answer}')
        ncr(n+1, answer, r)
    
    ncr(0, [], 3)
    
    cnt = 0
    for i in comb_list:
        if sum(i) == 0:
            cnt += 1
    
    return cnt

# def solution(number):
#     used = [0] * len(number)
    
#     # 순열
#     def permutation(array, n):
#         if n == len(number):
#             print(array)
#             return
#         for i in range(len(number)):
#             if not used[i]:
#                 used[i] = 1
#                 array.append(number[i])
#                 permutation(array, n+1)
#                 array.pop()
#                 used[i] = 0

#     permutation([], 0)    
#     return

# from itertools import combinations, permutations
# 참고 : https://velog.io/@sloools/Python-%EC%88%9C%EC%97%B4Permutation-%EC%A1%B0%ED%95%A9Combination

print(solution([-2, 3, 0, 2, -5]))
from itertools import permutations

def solution(numbers):
    answer = set()
    num_list = list(numbers)
    temp = []
    
    for i in range(1, len(numbers)+1):
        temp += list(permutations(num_list, i))
    
    num = [int(''.join(t)) for t in temp]
    
    for i in num:
        if is_prime(i):
            answer.add(i)
    return len(answer)

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
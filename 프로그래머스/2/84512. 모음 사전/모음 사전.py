from itertools import product

def solution(word):
    answer = []
    alphabet = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        for j in product(alphabet, repeat=i):
            answer.append(''.join(j))
    answer.sort()
    return answer.index(word) + 1
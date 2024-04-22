def solution(n):
    answer = 0
    base2_n = bin(n)[2:]
    cnt_n1 = base2_n.count('1')

    for i in range(n+1, 1000001):
        base2_i = bin(i)[2:]
        cnt_i1 = base2_i.count('1')
        if cnt_n1 == cnt_i1:
            answer = i
            break
    
    return answer
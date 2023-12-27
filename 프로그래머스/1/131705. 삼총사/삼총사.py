def solution(number):
    comb_list = []

    def ncr(n, answer, r):
        if n == len(number):
            if len(answer) == r:
                temp = [i for i in answer]
                comb_list.append(temp)
            return
        answer.append(number[n])
        ncr(n+1, answer, r)
        answer.pop()
        ncr(n+1, answer, r)
    
    ncr(0, [], 3)
    
    cnt = 0
    for i in comb_list:
        if sum(i) == 0:
            cnt += 1
    
    return cnt
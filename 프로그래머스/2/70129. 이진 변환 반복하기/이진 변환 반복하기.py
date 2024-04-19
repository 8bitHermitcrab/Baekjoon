def solution(s):
    cnt_base2 = 0
    cnt_0 = 0

    while len(s) > 1:
        ones = s.count('1')
        cnt_0 += s.count('0')
        s = str(bin(ones))[2:]
        cnt_base2 += 1

    answer = [cnt_base2, cnt_0]
    
    return answer
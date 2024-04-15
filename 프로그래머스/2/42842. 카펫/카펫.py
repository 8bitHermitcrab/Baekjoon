def solution(brown, yellow):
    answer = []
    total = yellow + brown
    
    for b in range(1, total+1):
        if (total / b) % 1 == 0:
            a = total // b
            if a >= b:
                if (a * 2) + (b * 2) == brown + 4:
                    return [a, b]
                
    return answer
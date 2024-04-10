def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for w in word:
            if w * 2 not in b:
                b = b.replace(w, '1')

        if b.isdigit():
            answer += 1
                     
    return answer
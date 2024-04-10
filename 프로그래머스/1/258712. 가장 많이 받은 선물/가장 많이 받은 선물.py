from collections import defaultdict

def solution(friends, gifts):
    # 선물 주고 받은 기록
    gifted = defaultdict(dict)
    score = defaultdict(int)
    for g in gifts:
        to, fr = g.split(" ")
        if fr in gifted[to]:
            gifted[to][fr] += 1
        else:
            gifted[to][fr] = 1
    
        # 선물지수
        score[to] += 1
        score[fr] -= 1
    
    cnt_gifts = [0 for _ in friends]
    for i in range(len(friends)):
        cur = friends[i]
        for j in range(i+1, len(friends)):
            another = friends[j]
            a = gifted[cur][another] if another in gifted[cur] else 0
            b = gifted[another][cur] if cur in gifted[another] else 0
            
            if a > b:
                cnt_gifts[i] += 1
            elif a < b:
                cnt_gifts[j] += 1
            elif a == b:
                a_score, b_score = score[cur], score[another]
                if a_score > b_score:
                    cnt_gifts[i] += 1
                elif a_score < b_score:
                    cnt_gifts[j] += 1
        
    answer = max(cnt_gifts)
    return answer
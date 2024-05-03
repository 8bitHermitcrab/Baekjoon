from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    for k in course:
        cand = []
        
        for menu_li in orders:
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                cand.append(res)
                
        sorted_cand = Counter(cand).most_common()
        answer += [menu for menu, cnt in sorted_cand if cnt > 1 and cnt == sorted_cand[0][1]]
    return sorted(answer)
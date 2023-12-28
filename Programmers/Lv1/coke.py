# 콜라 문제
def solution(a, b, n):
    answer = 0

    while n >= a:
        coke = n % a
        n = (n // a) * b    # 마트에서 받은 콜라의 수
        answer += n         # 받은 걸 answer에 +
        n += coke           # 남아있는 병을 더해줘서 다음에 마트갈 때 이용
    
    return answer

print(solution(3, 1, 20))
print(solution(2, 1, 20))

# 참고 : https://velog.io/@seulki971227/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-Lv.1-%EC%BD%9C%EB%9D%BC-%EB%AC%B8%EC%A0%9C-Python
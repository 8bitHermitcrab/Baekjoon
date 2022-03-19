# 부녀회장이 될 테야

# t : 테스트 케이스
t = int(input())
for _ in range(t):
    # k층
    k = int(input())
    # n호
    n = int(input())
    f = [x for x in range(1, n+1)]
    for _ in range(k):
        for i in range(1, n):
            f[i] += f[i-1]
        # 각 층의 1~5호실에 거주하는 사람 수를 리스트로 출력
        # print(f)
    print(f[-1])

    # k_n = (((k-1) * n)*(n-1)) / 2
    # print(k_n)

    # https://ooyoung.tistory.com/89
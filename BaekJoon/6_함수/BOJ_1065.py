# 한수

n = int(input())

def solve(n):
    ans = 0
    for i in range(1, n+1):
        n_list = list(map(int, str(i)))
        # 100보다 작으면 모두 한수
        if i < 100:
            ans += 1
        # n의 각 자리가 등차수열이면 한수
        elif n_list[0] - n_list[1] == n_list[1] - n_list[2]:
            ans += 1
    return ans

print(solve(n))



'''
https://beomjun0638.tistory.com/98
https://hello-bryan.tistory.com/293

https://ooyoung.tistory.com/65
'''
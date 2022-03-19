# ACM 호텔

# t개의 테스트 
t = int(input())
# h : 호텔의 층수, w : 각 층의 방수, n : n번째 손님
for _ in range(t):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h+1
    if a == 0:
       a = h
       b -= 1
    print(a*100 +b)

'''
https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-10250%EB%B2%88-ACM-%ED%98%B8%ED%85%94-in-python
'''
# 손익분기점

# a : 고정비용, b : 가변비용, c : 물건가격
a, b, c = map(int, input().split())

if b >= c :
    print(-1)
else:
    print((a//(c - b))+1)


'''
이익 = (1대 당 가격 C - 1대 당 생산비 B) * k 대 - 고정 비용 A
E = (C - B) * k - A

https://wlstyql.tistory.com/51
'''
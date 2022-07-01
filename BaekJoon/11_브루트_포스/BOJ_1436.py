# 영화감독 숌

n = int(input())

title = 666
count = 0 # 순번

while 1:
    # 666이 존재하면 순번 +1
    if '666' in str(title):
        count += 1
    # 순번이 n과 같다면 출력 후 break
    if count == n:
        print(title)
        break
    # 제목에 +1
    title += 1

# https://velog.io/@eazyan/%EB%B0%B1%EC%A4%80.-1436%EB%B2%88.-%EC%98%81%ED%99%94%EA%B0%90%EB%8F%85-%EC%88%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4
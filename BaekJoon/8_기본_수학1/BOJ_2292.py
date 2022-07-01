# 벌집

n = int(input())

# 벌집의 개수, 1개부터 시작
nums_bee_house = 1
count = 1
while n > nums_bee_house:
    # 벌집이 6의 배수로 증가
    nums_bee_house += 6 * count
    # 반복문 횟수
    count += 1
print(count)
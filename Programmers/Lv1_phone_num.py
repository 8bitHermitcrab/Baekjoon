# 핸드폰 번호 가리기

phone_number = '12345566'

answer = ''

len_phone_number = len(phone_number)

answer = '*' * (len_phone_number - 4)
print(answer)

answer += phone_number[-4:]
print(answer)


'''phone_number_f = phone_number[:-4]
print(phone_number_f)
phone_number_b = phone_number[-4:]
print(phone_number_b)

for i in range(len(phone_number_f)):
    temp = '*' * i
    answer = temp + phone_number_b
print(answer)'''

# https://somjang.tistory.com/entry/Programmers-%ED%95%B8%EB%93%9C%ED%8F%B0-%EB%B2%88%ED%98%B8-%EA%B0%80%EB%A6%AC%EA%B8%B0-Python
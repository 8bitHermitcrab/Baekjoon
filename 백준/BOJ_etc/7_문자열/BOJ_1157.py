# 단어 공부

word = input().upper()
# 입력받은 문자열에 있는 중복을 없앤 후에, 리스트 처리
unique_word = list(set(word))

count_list = []

# print(unique_word)

# 각 알파벳에 대한 개수를 센다
for i in unique_word:
    count = word.count(i)
    # print(count)
    count_list.append(count)
    # print(count_list)

# 최대값이 2개 이상일 경우 ? 출력
if count_list.count(max(count_list)) > 1:
    print('?')
# 알파벳 출력
else:
    max_index = count_list.index(max(count_list))
    # print(f'max_index = {max_index}')
    # print(f'unique_word = {unique_word}')
    print(unique_word[max_index])



'''
words = dict()

for i in range(len(word)):
    words[unique_word[i]] = unique_word.count(unique_word[i])
    # 딕셔너리에서 최대 값에 대한 키 찾기
    max_key = max(words, key=words.get)
print(max_key)
'''
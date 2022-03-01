'''오답 체크'''
# 그룹 단어 체커

n = int(input())
words = [input() for _ in range(n)]

group_word_count = 0

for i in range(n):
    for j in range(len(words[i])):
        print(words[i][j])

def group_word_check(word, alpa, count):
    word = list()
    alpabet = dict()
    alpabet[alpa] = count
    return 
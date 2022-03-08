'''오답 체크 - 풀이 이해 잘 안 됨'''
# 그룹 단어 체커

n = int(input())

group_word_count = 0

for i in range(n):
    words = input()
    for j in range(len(words)):
        if j != len(words)-1:
            if words[j] == words[j+1]:
                pass
            elif words[j] in words[j+1:]:
                break
        else:
            group_word_count +=1
print(group_word_count)

""" 
def group_word_check(alpa, count):
    # word = list()
    # words
    alpabet = dict()
    alpabet[alpa] = count
    return count 


    https://deokkk9.tistory.com/10
"""
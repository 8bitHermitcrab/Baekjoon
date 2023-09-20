# 문자열 폭발


words = input()
explo = input()

# mirkovC4
# C4
stack = []
explo_last = explo[-1]
len_explo = len(explo)

for word in words:
    stack.append(word)
    if word == explo_last and ''.join(stack[-len_explo:]) == explo:
        del stack[-len_explo:]

answer = ''.join(stack)

if answer == '':
    print('FRULA')
else:
    print(answer)

'''
https://mytodays.tistory.com/23
'''
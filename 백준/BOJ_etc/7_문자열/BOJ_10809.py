# 알파벳 찾기


S = input()

alpabet = 'abcdefghijklmnopqrstuvwxyz'

idx_dic = dict()

for i in range(26):
    idx_dic[alpabet[i]] = -1
    idx = S.find(alpabet[i])
    idx_dic[alpabet[i]] = idx


for value in idx_dic.values():
    print(value, end=' ')
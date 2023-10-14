word = input()

alpabat = [0] * 26

for i in word:
    alpabat[ord(i) - 97] += 1

print(*alpabat)
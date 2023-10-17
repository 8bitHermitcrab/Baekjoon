sent = input()
result = []

def rot13(n):
    if ord(n) == 32 or (ord(n) >= 48 and ord(n) <= 57):
        x = ord(n)
        result.append(chr(x))
    else:
        if n.isupper() == True:
            n = n.lower()
            x = ord(n) + 13
            if x > 122:
                x = (x - 122) + 96
            result.append(chr(x).upper())
        else:
            x = ord(n) + 13
            if x > 122:
                x = (x - 122) + 96
            result.append(chr(x))

for i in sent:
    rot13(i)

print(''.join(result))